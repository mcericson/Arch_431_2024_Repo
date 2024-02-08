let img;
let pixelColors = [];
let density = 5;
let rValues = [];

function preload() {
    img = loadImage('web_mountains_small.jpg');

}

function setup() {
    // put setup code here
    createCanvas(windowWidth, windowHeight, WEBGL);
    background(255)
    for (let i = 0; i < img.width; i += density) {
        for (let j = 0; j < img.height; j += density) {
            let x = i;
            let y = j;
            let c = img.get(x, y)
            pixelColors.push(c);
            rValues.push(c[0]);

        }
    }
}

function draw() {
    scale(2.0);
    background(pixelColors[1]);
    orbitControl();
    let distance = dist(0, 0, mouseX, mouseY)
    let rand = random(-1.0, 1.0);
    randomMove = distance / width
    pixelBoxes(img, density, rValues, randomMove);


}

function pixelBoxes(img, density, rValues, move) {

    count = 0;
    for (let i = 0; i < img.width; i += density) {
        for (let j = 0; j < img.height; j += density) {
            count += 1;
            let x = i;
            let y = j;
            noStroke();
            let col = pixelColors[count];
            if (count < pixelColors.length) {
                fill(col);
                let zVal = rValues[count] * move;
                translate(x, y, zVal);
                box(density);
                translate(-x, -y, -zVal);
            }

        }

    }
}