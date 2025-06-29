closet = [
    # Plain White Target Crop top
    {
        "name": "White Crop Top",
        "article": "tops",
        "styleTags": ["neutral", "basic", "comfy"],
        "seasonTags": ["spring", "summer", "fall"],
        "indoorOnly": False,
        "minTemp": 55,
        "maxTemp": 100,
        "color": "white",
        "pattern": ["solid", "plain"],
        "material": "cotton"
    },

    # Doc Martens Oxford
    {
        "name": "Docs",
        "article": "shoes",
        "styleTags": ["neutral", "edgy", "grunge"],
        "seasonTags": ["spring", "summer", "fall", "winter"],
        "weatherTags": ["sunny", "rainy", "windy", "cloudy", "snowing", "freezing"],
        "indoorOnly": False,
        "minTemp": 20,
        "maxTemp": 100,
        "color": "black",
        "pattern": ["solid", "plain"],
        "material": "rubber"
    },

    # Abercrombie Medium Wash Solid Jeans
    {
        "name": "High Waisted Medium Wash Jeans",
        "article": "bottoms",
        "styleTags": ["neutral", "basic", "comfy", "casual"],
        "seasonTags": ["spring", "summer", "fall"],
        "weatherTags": ["sunny", "rainy", "windy", "cloudy", "snowing", "freezing"],
        "indoorOnly": False,
        "minTemp": 20,
        "maxTemp": 90,
        "color": "blue",
        "pattern": ["solid", "plain"],
        "material": "denim"
    }

]


#testing   
for item in closet:
    print(f"{item['name']} {item['article']} - {item['material']} ({item['color']})")


#filtering style

