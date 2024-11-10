'use client'

import { useState } from 'react'
import { Link } from 'react-router-dom'
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Checkbox } from "@/components/ui/checkbox"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Textarea } from "@/components/ui/textarea"
import { ScrollArea } from "@/components/ui/scroll-area"
import ToolRecommendations from './ToolRecommendations'

const categories = [
  "Machine Learning Optimization", "Energy-Efficient NLP", "Green Computer Vision",
  "Sustainable Edge Computing", "Resource-Optimized Deep Learning", 
  "Eco-Friendly Data Processing", "Smart Grid AI", "Waste Management AI",
  "Renewable Energy AI", "Carbon Footprint Analytics", "Environmental Monitoring",
  "Green Cloud Computing", "Sustainable IoT", "Energy Management Systems",
  "Resource Planning AI", "Climate Modeling AI", "Eco-Logistics AI",
  "Green Manufacturing AI", "Sustainable Agriculture AI", "Water Management AI"
]

export default function EcoAIFinder() {
  const [step, setStep] = useState(0)
  const [userResponses, setUserResponses] = useState({
    focus: '',
    categories: [],
    industry: '',
    metrics: [],
    integrations: '',
  })
  const [recommendations, setRecommendations] = useState([])
  const [selectedCategory, setSelectedCategory] = useState('')
  const [selectedPreference, setSelectedPreference] = useState('')
  const [searchTerm, setSearchTerm] = useState('')

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setUserResponses(prev => ({ ...prev, [name]: value }))
    
    if (name === 'focus') {
      setSelectedPreference(value)
      const input_json = JSON.stringify({
        "category": selectedCategory,
        "preference": value
      })
      console.log(input_json)
    }
  }

  const handleCheckboxChange = (field, value) => {
    setUserResponses(prev => ({
      ...prev,
      [field]: prev[field].includes(value)
        ? prev[field].filter(item => item !== value)
        : [...prev[field], value]
    }))
    
    if (field === 'categories') {
      setSelectedCategory(value)
      const input_json = JSON.stringify({
        "category": value,
        "preference": selectedPreference || "mix"
      })
      console.log(input_json)
    }
  }

  const generateRecommendations = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/recommendations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          "category": selectedCategory,
          "preference": selectedPreference
        })
      })
      const data = await response.json()
      setRecommendations(data.recommendations)
      setStep(5)
    } catch (error) {
      console.error('Error fetching recommendations:', error)
      const sampleData = {
        "recommendations": [
          {
              "Tool": "Google Cloud IoT",
              "Score": 7.403348017621146,
              "Accuracy": 9.0,
              "Speed": 8.7,
              "Energy Efficiency": 9.2,
              "Carbon Footprint": 9.1,
              "Waste Reduction": 9.0,
              "Energy Consumption": 8.6,
              "Resource Efficiency": 9.3,
              "Water Usage": 5.0,
              "Lifetime Durability": 9.2
          },
          {
              "Tool": "Microsoft Azure IoT",
              "Score": 7.3189427312775335,
              "Accuracy": 8.9,
              "Speed": 8.6,
              "Energy Efficiency": 9.1,
              "Carbon Footprint": 9.2,
              "Waste Reduction": 8.9,
              "Energy Consumption": 8.5,
              "Resource Efficiency": 9.1,
              "Water Usage": 5.0,
              "Lifetime Durability": 9.1
          },
          {
              "Tool": "AWS IoT Greengrass",
              "Score": 7.247111111111112,
              "Accuracy": 8.8,
              "Speed": 8.5,
              "Energy Efficiency": 9.3,
              "Carbon Footprint": 9.1,
              "Waste Reduction": 9.0,
              "Energy Consumption": 8.4,
              "Resource Efficiency": 9.2,
              "Water Usage": 5.0,
              "Lifetime Durability": 9.3
          }
      ]
      }
      setRecommendations(sampleData.recommendations)
      setStep(5)
    }
  }

  const renderStep = () => {
    switch (step) {
      case 0:
        return (
          <Card className="w-full max-w-md mx-auto p-5 border border-gray-300">
            <CardHeader>
              <CardTitle className="text-2xl">Welcome to Eco-AI Finder!</CardTitle>
              <CardDescription className="text-xl">Let's find the best sustainable AI tools tailored to your needs.</CardDescription>
            </CardHeader>
            <CardContent className="text-xl">
              <p>We'll ask you a few questions to understand your requirements and sustainability goals.</p>
            </CardContent>
            <CardFooter className="flex justify-between">
              <Link to="/">
                <Button>Back</Button>
              </Link>
              <Button className="bg-black text-white" onClick={() => setStep(1)}>Next</Button>
            </CardFooter>
          </Card>
        )
      case 1:
        return (
          <Card className="w-full max-w-md mx-auto p-5 border border-gray-300">
            <CardHeader>
              <CardTitle className="text-2xl">Select AI Categories</CardTitle>
              <CardDescription className="text-xl">Choose the categories that best fit your project needs</CardDescription>
            </CardHeader>
            <CardContent className="text-xl">
              <Input 
                type="text" 
                placeholder="Search categories..." 
                value={searchTerm} 
                onChange={(e) => setSearchTerm(e.target.value)} 
                className="mb-4"
              />
              <ScrollArea className="h-[300px] pr-4">
                {categories.filter(category => category.toLowerCase().includes(searchTerm.toLowerCase())).map((category) => (
                  <div key={category} className="flex items-center space-x-2 mb-2">
                    <Checkbox
                      id={category}
                      checked={userResponses.categories.includes(category)}
                      onCheckedChange={() => handleCheckboxChange('categories', category)}
                    />
                    <Label htmlFor={category}>{category}</Label>
                  </div>
                ))}
              </ScrollArea>
            </CardContent>
            <CardFooter className="flex justify-between">
              <Button onClick={() => setStep(0)}>Back</Button>
              <Button className="bg-black text-white" onClick={() => setStep(2)}>Next</Button>
            </CardFooter>
          </Card>
        )
      case 2:
        return (
          <Card className="w-full max-w-md mx-auto p-5 border border-gray-300">
            <CardHeader>
              <CardTitle className="text-2xl">What's your main focus?</CardTitle>
            </CardHeader>
            <CardContent className="text-xl">
              <RadioGroup name="focus" onValueChange={(value) => handleInputChange({ target: { name: 'focus', value } })}>
                <div className="flex items-center space-x-2">
                  <RadioGroupItem value="energy efficiency" id="energy" />
                  <Label htmlFor="energy">Energy Efficiency</Label>
                </div>
                <div className="flex items-center space-x-2">
                  <RadioGroupItem value="waste reduction" id="waste" />
                  <Label htmlFor="waste">Accuracy</Label>
                </div>
                <div className="flex items-center space-x-2">
                  <RadioGroupItem value="resource management" id="resource" />
                  <Label htmlFor="resource">Balanced</Label>
                </div>
              </RadioGroup>
            </CardContent>
            <CardFooter className="flex justify-between">
              <Button onClick={() => setStep(1)}>Back</Button>
              <Button className="bg-black text-white" onClick={generateRecommendations}>Find Eco-AI Tools</Button>
            </CardFooter>
          </Card>
        )
      case 5:
        return (
          <ToolRecommendations recommendations={recommendations} />
        )
    }
  }

  return (
    <div className="flex items-center justify-center min-h-screen">
      {renderStep()}
    </div>
  )
}