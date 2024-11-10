import React, { useState } from "react";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import {
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import ToolRecommendations from "./ToolRecommendations";

export default function TextAi() {
  const [userResponses, setUserResponses] = useState({
    focus: "",
    categories: [],
    industry: "",
    metrics: [],
    integrations: "",
  });
  const [recommendations, setRecommendations] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUserResponses((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async () => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch("http://127.0.0.1:8001/recommendations/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_query: userResponses.focus,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to fetch recommendations.");
      }

      const data = await response.json();
      setRecommendations(data.recommendations);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setUserResponses({
      focus: "",
      categories: [],
      industry: "",
      metrics: [],
      integrations: "",
    });
    setRecommendations([]);
    setError(null);
  };

  return (
    <div>
      <CardHeader>
        <CardTitle>Ask AI</CardTitle>
      </CardHeader>
      <CardContent>
        <Textarea
          name="focus"
          value={userResponses.focus}
          onChange={handleInputChange}
          placeholder="Please recommend tools for energy-efficient machine learning with a focus on accuracy."
        />
      </CardContent>
      <CardFooter className="flex justify-between">
        <Link to="/">
          <Button className="bg-white text-black">
            Back
          </Button>
        </Link>
        <Button
          onClick={handleSubmit}
          disabled={isLoading}
          className="bg-black text-white hover:bg-white hover:text-black"
        >
          {isLoading ? "Loading..." : "Get Recommendations"}
        </Button>
        {recommendations.length > 0 && (
          <Button
            onClick={handleReset}
            className="bg-black text-white hover:bg-white hover:text-black"
          >
            Enter New Prompt
          </Button>
        )}
      </CardFooter>
      {error && <p className="text-red-500 mt-4">{error}</p>}

      {/* Render ToolRecommendations if recommendations are available */}
      {recommendations.length > 0 && (
        <ToolRecommendations recommendations={recommendations} />
      )}
    </div>
  );
}