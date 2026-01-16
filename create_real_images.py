from PIL import Image, ImageDraw, ImageFont
import os

def create_habitat_map():
    width, height = 800, 500
    img = Image.new('RGB', (width, height), '#2c3e50')
    draw = ImageDraw.Draw(img)
    
    draw.ellipse([100, 150, 250, 300], fill='#27ae60', outline='#2ecc71', width=2)
    draw.ellipse([300, 100, 450, 250], fill='#e74c3c', outline='#c0392b', width=2)
    draw.ellipse([500, 120, 650, 270], fill='#f39c12', outline='#e67e22', width=2)
    draw.ellipse([200, 320, 350, 470], fill='#3498db', outline='#2980b9', width=2)
    draw.ellipse([450, 300, 600, 450], fill='#9b59b6', outline='#8e44ad', width=2)
    draw.ellipse([620, 280, 780, 430], fill='#1abc9c', outline='#16a085', width=2)
    
    try:
        font = ImageFont.truetype("arial.ttf", 14)
        title_font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((400, 30), "Cat Species Population Density", fill='white', font=title_font, anchor='mm')
    draw.text((175, 225), "North America", fill='white', font=font, anchor='mm')
    draw.text((375, 175), "Europe", fill='white', font=font, anchor='mm')
    draw.text((575, 195), "Asia", fill='white', font=font, anchor='mm')
    draw.text((275, 395), "South America", fill='white', font=font, anchor='mm')
    draw.text((525, 375), "Africa", fill='white', font=font, anchor='mm')
    draw.text((700, 355), "Australia", fill='white', font=font, anchor='mm')
    
    legend_y = 460
    draw.rectangle([50, 440, 70, 460], fill='#e74c3c')
    draw.text((80, 450), "High Density", fill='white', font=font, anchor='lm')
    draw.rectangle([200, 440, 220, 460], fill='#f39c12')
    draw.text((230, 450), "Medium-High", fill='white', font=font, anchor='lm')
    draw.rectangle([350, 440, 370, 460], fill='#27ae60')
    draw.text((380, 450), "Medium", fill='white', font=font, anchor='lm')
    draw.rectangle([480, 440, 500, 460], fill='#3498db')
    draw.text((510, 450), "Low", fill='white', font=font, anchor='lm')
    
    img.save('images/habitat-map.jpg', 'JPEG', quality=95)

def create_endangered_species():
    width, height = 600, 400
    img = Image.new('RGB', (width, height), '#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([50, 50, 280, 200], fill='#e74c3c', outline='#c0392b', width=3)
    draw.rectangle([320, 50, 550, 200], fill='#f39c12', outline='#e67e22', width=3)
    draw.rectangle([50, 220, 280, 370], fill='#3498db', outline='#2980b9', width=3)
    draw.rectangle([320, 220, 550, 370], fill='#9b59b6', outline='#8e44ad', width=3)
    
    try:
        font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((300, 25), "Endangered Species Categories", fill='white', font=title_font, anchor='mm')
    
    draw.text((165, 125), "Critically Endangered", fill='white', font=font, anchor='mm')
    draw.text((165, 145), "CR", fill='white', font=title_font, anchor='mm')
    
    draw.text((435, 125), "Endangered", fill='white', font=font, anchor='mm')
    draw.text((435, 145), "EN", fill='white', font=title_font, anchor='mm')
    
    draw.text((165, 295), "Vulnerable", fill='white', font=font, anchor='mm')
    draw.text((165, 315), "VU", fill='white', font=title_font, anchor='mm')
    
    draw.text((435, 295), "Near Threatened", fill='white', font=font, anchor='mm')
    draw.text((435, 315), "NT", fill='white', font=title_font, anchor='mm')
    
    img.save('images/endangered-species.jpg', 'JPEG', quality=95)

def create_deforestation():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), '#87CEEB')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([0, 250, 500, 350], fill='#8B4513')
    
    for i in range(5):
        x = 30 + i * 90
        draw.rectangle([x, 200, x+20, 250], fill='#654321')
        draw.ellipse([x-20, 150, x+40, 210], fill='#228B22')
    
    for i in range(3):
        x = 400 + i * 40
        draw.rectangle([x, 230, x+15, 250], fill='#654321')
        draw.ellipse([x-15, 190, x+30, 240], fill='#32CD32')
    
    draw.polygon([100, 250, 150, 250, 125, 200], fill='#D2691E')
    draw.polygon([150, 250, 200, 250, 175, 210], fill='#CD853F')
    draw.polygon([200, 250, 250, 250, 225, 195], fill='#DEB887')
    
    try:
        font = ImageFont.truetype("arial.ttf", 14)
        title_font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((250, 30), "Deforestation Impact", fill='white', font=title_font, anchor='mm')
    draw.text((250, 280), "Deforested Area", fill='white', font=font, anchor='mm')
    
    img.save('images/deforestation.jpg', 'JPEG', quality=95)

def create_habitat_fragmentation():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), '#2c3e50')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([20, 20, 180, 150], fill='#27ae60', outline='#2ecc71', width=2)
    draw.rectangle([200, 20, 350, 120], fill='#27ae60', outline='#2ecc71', width=2)
    draw.rectangle([370, 30, 480, 130], fill='#27ae60', outline='#2ecc71', width=2)
    draw.rectangle([30, 170, 150, 280], fill='#27ae60', outline='#2ecc71', width=2)
    draw.rectangle([200, 150, 320, 250], fill='#27ae60', outline='#2ecc71', width=2)
    draw.rectangle([360, 160, 470, 270], fill='#27ae60', outline='#2ecc71', width=2)
    draw.rectangle([50, 300, 180, 330], fill='#27ae60', outline='#2ecc71', width=2)
    draw.rectangle([250, 280, 400, 330], fill='#27ae60', outline='#2ecc71', width=2)
    
    draw.line([(180, 100), (200, 80)], fill='#e74c3c', width=4)
    draw.line([(350, 80), (370, 90)], fill='#e74c3c', width=4)
    draw.line([(150, 220), (200, 200)], fill='#e74c3c', width=4)
    draw.line([(320, 200), (360, 220)], fill='#e74c3c', width=4)
    draw.line([(180, 280), (250, 300)], fill='#e74c3c', width=4)
    
    try:
        font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((250, 345), "Habitat Fragmentation", fill='white', font=title_font, anchor='mm')
    
    img.save('images/habitat-fragmentation.jpg', 'JPEG', quality=95)

def create_poaching():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), '#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    draw.ellipse([100, 100, 200, 200], fill='#95a5a6')
    draw.ellipse([110, 90, 130, 110], fill='#7f8c8d')
    draw.ellipse([170, 90, 190, 110], fill='#7f8c8d')
    draw.ellipse([145, 140, 155, 150], fill='#2c3e50')
    draw.polygon([100, 180, 150, 200, 200, 180], fill='#7f8c8d')
    
    draw.line([280, 150, 420, 150], fill='#c0392b', width=3)
    draw.line([350, 100, 350, 200], fill='#c0392b', width=3)
    draw.ellipse([340, 90, 360, 110], fill='#e74c3c')
    
    draw.rectangle([400, 250, 480, 300], fill='#e74c3c', outline='#c0392b', width=2)
    
    try:
        font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((250, 30), "Illegal Poaching", fill='white', font=title_font, anchor='mm')
    draw.text((440, 275), "ILLEGAL", fill='white', font=font, anchor='mm')
    draw.text((150, 250), "Rhino", fill='white', font=font, anchor='mm')
    
    img.save('images/poaching.jpg', 'JPEG', quality=95)

def create_bycatch():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), '#1e3a5f')
    draw = ImageDraw.Draw(img)
    
    draw.line([50, 200, 450, 200], fill='#95a5a6', width=2)
    for i in range(8):
        x = 70 + i * 50
        draw.line([x, 180, x, 220], fill='#7f8c8d', width=1)
    
    draw.ellipse([100, 180, 140, 220], fill='#3498db')
    draw.ellipse([200, 170, 240, 210], fill='#e74c3c')
    draw.ellipse([300, 175, 340, 215], fill='#2ecc71')
    draw.ellipse([380, 185, 420, 225], fill='#f39c12')
    
    draw.polygon([120, 190, 130, 185, 140, 190, 130, 195], fill='white')
    draw.polygon([220, 180, 230, 175, 240, 180, 230, 185], fill='white')
    
    try:
        font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((250, 30), "Bycatch in Fishing Nets", fill='white', font=title_font, anchor='mm')
    draw.text((250, 280), "Marine Species Caught Accidentally", fill='white', font=font, anchor='mm')
    
    img.save('images/bycatch.jpg', 'JPEG', quality=95)

def create_overfishing():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), '#1e3a5f')
    draw = ImageDraw.Draw(img)
    
    for i in range(10):
        x = 50 + i * 40
        y = 100 + (i % 3) * 30
        draw.ellipse([x, y, x+30, y+15], fill='#3498db')
        draw.polygon([x+5, y+5, x+10, y+2, x+15, y+5], fill='#2c3e50')
    
    for i in range(5):
        x = 100 + i * 60
        y = 200 + (i % 2) * 40
        draw.ellipse([x, y, x+25, y+12], fill='#e74c3c')
        draw.polygon([x+5, y+4, x+8, y+2, x+11, y+4], fill='#2c3e50')
    
    draw.line([0, 300, 500, 300], fill='#c0392b', width=3)
    
    try:
        font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((250, 30), "Overfishing Crisis", fill='white', font=title_font, anchor='mm')
    draw.text((250, 325), "Depleted Fish Populations", fill='white', font=font, anchor='mm')
    
    img.save('images/overfishing.jpg', 'JPEG', quality=95)

def create_pollution():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), '#2c3e50')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([50, 200, 150, 300], fill='#7f8c8d')
    for i in range(3):
        y = 150 + i * 50
        draw.rectangle([60, y, 140, y+40], fill='#34495e')
    
    draw.ellipse([120, 130, 180, 180], fill='#95a5a6')
    draw.ellipse([130, 110, 170, 140], fill='#7f8c8d')
    draw.ellipse([135, 100, 165, 120], fill='#6c7a7d')
    
    for i in range(5):
        x = 200 + i * 60
        y = 280 + (i % 2) * 30
        draw.rectangle([x, y, x+40, y+30], fill='#e74c3c')
    
    draw.line([0, 320, 500, 320], fill='#2980b9', width=5)
    
    try:
        font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((250, 30), "Industrial Pollution", fill='white', font=title_font, anchor='mm')
    draw.text((250, 340), "Water and Air Contamination", fill='white', font=font, anchor='mm')
    
    img.save('images/pollution.jpg', 'JPEG', quality=95)

def create_drought():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), '#f39c12')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([0, 250, 500, 350], fill='#d35400')
    
    draw.ellipse([50, 200, 100, 240], fill='#e67e22')
    draw.rectangle([70, 230, 80, 250], fill='#d35400')
    
    draw.ellipse([150, 190, 200, 230], fill='#e67e22')
    draw.rectangle([170, 220, 180, 250], fill='#d35400')
    
    draw.ellipse([300, 180, 380, 240], fill='#e67e22')
    draw.rectangle([330, 230, 350, 250], fill='#d35400')
    
    draw.line([0, 100, 500, 100], fill='#e74c3c', width=3)
    
    for i in range(8):
        x = 30 + i * 60
        draw.line([x, 50, x, 100], fill='#f39c12', width=2)
    
    try:
        font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((250, 30), "Severe Drought Conditions", fill='white', font=title_font, anchor='mm')
    draw.text((250, 300), "Cracked Dry Earth", fill='white', font=font, anchor='mm')
    
    img.save('images/drought.jpg', 'JPEG', quality=95)

def create_oil_gas_development():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), '#2c3e50')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([50, 150, 100, 300], fill='#7f8c8d')
    draw.polygon([50, 150, 75, 100, 100, 150], fill='#95a5a6')
    draw.rectangle([70, 120, 80, 150], fill='#e74c3c')
    
    draw.rectangle([150, 180, 200, 300], fill='#7f8c8d')
    draw.polygon([150, 180, 175, 130, 200, 180], fill='#95a5a6')
    draw.rectangle([170, 150, 180, 180], fill='#f39c12')
    
    draw.ellipse([300, 200, 400, 280], fill='#34495e')
    draw.ellipse([320, 180, 380, 220], fill='#2c3e50')
    draw.rectangle([345, 150, 355, 180], fill='#e74c3c')
    
    draw.line([420, 250, 480, 250], fill='#e74c3c', width=5)
    draw.line([450, 220, 450, 280], fill='#e74c3c', width=5)
    
    try:
        font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((250, 30), "Oil & Gas Development", fill='white', font=title_font, anchor='mm')
    draw.text((450, 265), "⚠", fill='white', font=title_font, anchor='mm')
    
    img.save('images/oil-gas-development.jpg', 'JPEG', quality=95)

def create_soil_erosion():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), '#8B4513')
    draw = ImageDraw.Draw(img)
    
    draw.polygon([0, 150, 100, 50, 200, 100, 300, 30, 400, 80, 500, 60, 500, 350, 0, 350], fill='#A0522D')
    
    draw.line([50, 200, 100, 180], fill='#654321', width=3)
    draw.line([150, 220, 200, 190], fill='#654321', width=3)
    draw.line([250, 200, 300, 170], fill='#654321', width=3)
    draw.line([350, 210, 400, 180], fill='#654321', width=3)
    draw.line([420, 230, 470, 200], fill='#654321', width=3)
    
    draw.ellipse([100, 280, 150, 320], fill='#D2691E')
    draw.ellipse([250, 290, 300, 330], fill='#CD853F')
    draw.ellipse([380, 270, 430, 310], fill='#DEB887')
    
    try:
        font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((250, 30), "Soil Erosion", fill='white', font=title_font, anchor='mm')
    draw.text((250, 335), "Topsoil Loss", fill='white', font=font, anchor='mm')
    
    img.save('images/soil-erosion.jpg', 'JPEG', quality=95)

def create_soil_degradation():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), '#5D4037')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([50, 50, 200, 150], fill='#8D6E63')
    draw.rectangle([250, 80, 400, 180], fill='#795548')
    draw.rectangle([100, 200, 300, 300], fill='#6D4C41')
    
    draw.line([100, 120, 150, 100], fill='#4E342E', width=2)
    draw.line([300, 150, 350, 130], fill='#4E342E', width=2)
    draw.line([180, 270, 230, 250], fill='#4E342E', width=2)
    
    for i in range(10):
        x = 50 + i * 45
        y = 320 + (i % 2) * 20
        draw.ellipse([x, y, x+15, y+25], fill='#A1887F')
    
    try:
        font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((250, 30), "Soil Degradation", fill='white', font=title_font, anchor='mm')
    draw.text((250, 340), "Reduced Soil Quality", fill='white', font=font, anchor='mm')
    
    img.save('images/soil-degradation.jpg', 'JPEG', quality=95)

def create_conservation_action():
    width, height = 600, 400
    img = Image.new('RGB', (width, height), '#27ae60')
    draw = ImageDraw.Draw(img)
    
    draw.ellipse([50, 50, 150, 150], fill='#2ecc71', outline='#1abc9c', width=3)
    draw.ellipse([175, 50, 275, 150], fill='#3498db', outline='#2980b9', width=3)
    draw.ellipse([300, 50, 400, 150], fill='#9b59b6', outline='#8e44ad', width=3)
    draw.ellipse([425, 50, 525, 150], fill='#e74c3c', outline='#c0392b', width=3)
    
    draw.ellipse([112, 200, 212, 300], fill='#f39c12', outline='#e67e22', width=3)
    draw.ellipse([237, 200, 337, 300], fill='#1abc9c', outline='#16a085', width=3)
    draw.ellipse([362, 200, 462, 300], fill='#34495e', outline='#2c3e50', width=3)
    
    try:
        font = ImageFont.truetype("arial.ttf", 10)
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    draw.text((300, 25), "Conservation Actions", fill='white', font=title_font, anchor='mm')
    
    draw.text((100, 100), "Habitat", fill='white', font=font, anchor='mm')
    draw.text((100, 115), "Protection", fill='white', font=font, anchor='mm')
    
    draw.text((225, 100), "Anti-Poaching", fill='white', font=font, anchor='mm')
    draw.text((225, 115), "Efforts", fill='white', font=font, anchor='mm')
    
    draw.text((350, 100), "Species", fill='white', font=font, anchor='mm')
    draw.text((350, 115), "Breeding", fill='white', font=font, anchor='mm')
    
    draw.text((475, 100), "Public", fill='white', font=font, anchor='mm')
    draw.text((475, 115), "Education", fill='white', font=font, anchor='mm')
    
    draw.text((162, 250), "Sustainable", fill='white', font=font, anchor='mm')
    draw.text((162, 265), "Practices", fill='white', font=font, anchor='mm')
    
    draw.text((287, 250), "Legal", fill='white', font=font, anchor='mm')
    draw.text((287, 265), "Protection", fill='white', font=font, anchor='mm')
    
    draw.text((412, 250), "Research", fill='white', font=font, anchor='mm')
    draw.text((412, 265), "& Monitoring", fill='white', font=font, anchor='mm')
    
    draw.text((300, 350), "Together We Can Protect Wildlife", fill='white', font=title_font, anchor='mm')
    
    img.save('images/conservation-action.jpg', 'JPEG', quality=95)

if __name__ == '__main__':
    os.makedirs('images', exist_ok=True)
    
    create_habitat_map()
    print("Created habitat-map.jpg")
    
    create_endangered_species()
    print("Created endangered-species.jpg")
    
    create_deforestation()
    print("Created deforestation.jpg")
    
    create_habitat_fragmentation()
    print("Created habitat-fragmentation.jpg")
    
    create_poaching()
    print("Created poaching.jpg")
    
    create_bycatch()
    print("Created bycatch.jpg")
    
    create_overfishing()
    print("Created overfishing.jpg")
    
    create_pollution()
    print("Created pollution.jpg")
    
    create_drought()
    print("Created drought.jpg")
    
    create_oil_gas_development()
    print("Created oil-gas-development.jpg")
    
    create_soil_erosion()
    print("Created soil-erosion.jpg")
    
    create_soil_degradation()
    print("Created soil-degradation.jpg")
    
    create_conservation_action()
    print("Created conservation-action.jpg")
    
    print("\nAll images created successfully!")