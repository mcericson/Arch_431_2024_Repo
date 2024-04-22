let img;
let pixelColors = [];
let density = 5;
let zValues = [];

function preload() {
    img = loadImage('web_mountains_small.jpg');

}

function setup() {
    // put setup code here
    createCanvas(windowWidth, windowHeight);
    background(255)
    let w = img.width / 2
    let h = img.height / 2
        //run loop to get pixel color values and z values before draw loop to prevent lag
    for (let i = 0; i < 10 * w; i += w) {
        for (let j = 0; j < 10 * h; j += h) {
            let x = i;
            let y = j;

            image(img, x, y, w, h)


        }
    }
}

function draw() {
    scale(2.0);
    background(pixelColors[1]);
    orbitControl();
    //call the pixelBoxes() function to render the boxes to the screen in the draw loop
    pixelBoxes(img, density, zValues);


}

function pixelBoxes(img, density, zValues) {

    count = 0;
    for (let i = 0; i < img.width; i += density) {
        for (let j = 0; j < img.height; j += density) {
            count += 1;
            let x = i;
            let y = j;
            //let newPoint = projectToSphere([0, 0, 0], [x, y, 0], 300);
            noStroke();
            let col = pixelColors[count];
            if (count < pixelColors.length) {
                fill(col);
                let zVal = zValues[count];
                translate(x, y, zVal);
                box(density);
                translate(-x, -y, -zVal);
            }

        }

    }
}

function projectToSphere(center, point, radius) {

    let cx = center[0];
    let cy = center[1];
    let cz = center[2];
    let x = point[0]
    let y = point[1]
    let z = point[2]

    let b_side = dist(cx, cy, cz, x, y, z);
    let c_side = radius;
    let a_side = Math.sqrt(Math.abs(b_side * b_side - c_side * c_side));
    let z1 = a_side;


    return [x, y, z1]
}