let boxNum = 10;
let cubeDim = 20;

function setup() {
    // put setup code here
    createCanvas(windowWidth, windowHeight, WEBGL);
    background(255)
    colorMode(RGB, boxNum)

}

function draw() {
    background(255);
    // put drawing code here
    angle = radians(frameCount);
    rotateX(angle);
    rotateZ(angle);
    cubic_grid(boxNum, boxNum, boxNum, cubeDim);


}

function cubic_grid(x_num, y_num, z_num, edgeDim) {
    scale(edgeDim);
    for (let i = 0; i < x_num; i++) {
        for (let j = 0; j < y_num; j++) {
            for (let p = 0; p < z_num; p++) {
                let x = i
                let y = j;
                let z = p;
                noStroke()
                fill(x, y, z)
                translate(x, y, z)
                box(1);
                translate(-x, -y, -z)



            }
        }
    }
}