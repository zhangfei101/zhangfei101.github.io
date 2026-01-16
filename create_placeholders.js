const fs = require('fs');
const path = require('path');

// 确保images目录存在
const imagesDir = path.join(__dirname, 'images');
if (!fs.existsSync(imagesDir)) {
    fs.mkdirSync(imagesDir);
}

// 简单的SVG图片数据（转换为base64）
const imagesData = [
    {
        filename: 'habitat-map.jpg',
        svg: `<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="800" height="500" fill="#4a7c59"/><text x="400" y="250" font-family="Arial, sans-serif" font-size="30" fill="white" text-anchor="middle">Habitat Map</text></svg>`
    },
    {
        filename: 'endangered-species.jpg', 
        svg: `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400" viewBox="0 0 600 400"><rect width="600" height="400" fill="#e74c3c"/><text x="300" y="200" font-family="Arial, sans-serif" font-size="30" fill="white" text-anchor="middle">Endangered Species</text></svg>`
    },
    {
        filename: 'deforestation.jpg',
        svg: `<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300"><rect width="400" height="300" fill="#f39c12"/><text x="200" y="150" font-family="Arial, sans-serif" font-size="24" fill="white" text-anchor="middle">Deforestation</text></svg>`
    },
    {
        filename: 'habitat-fragmentation.jpg',
        svg: `<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300"><rect width="400" height="300" fill="#e67e22"/><text x="200" y="150" font-family="Arial, sans-serif" font-size="24" fill="white" text-anchor="middle">Habitat Fragmentation</text></svg>`
    },
    {
        filename: 'poaching.jpg',
        svg: `<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300"><rect width="400" height="300" fill="#c0392b"/><text x="200" y="150" font-family="Arial, sans-serif" font-size="24" fill="white" text-anchor="middle">Poaching</text></svg>`
    },
    {
        filename: 'pollution.jpg',
        svg: `<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300"><rect width="400" height="300" fill="#8e44ad"/><text x="200" y="150" font-family="Arial, sans-serif" font-size="24" fill="white" text-anchor="middle">Pollution</text></svg>`
    },
    {
        filename: 'conservation-action.jpg',
        svg: `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400" viewBox="0 0 600 400"><rect width="600" height="400" fill="#27ae60"/><text x="300" y="200" font-family="Arial, sans-serif" font-size="30" fill="white" text-anchor="middle">Conservation Action</text></svg>`
    }
];

// 将SVG转换为Buffer并写入文件
imagesData.forEach(data => {
    const filePath = path.join(imagesDir, data.filename);
    // 将SVG转换为Buffer
    const buffer = Buffer.from(data.svg);
    fs.writeFileSync(filePath, buffer);
    console.log(`Created ${data.filename}`);
});

console.log('All placeholder images have been created successfully!');