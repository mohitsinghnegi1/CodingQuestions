interface Shape {
    getArea(): number;
    printType(): void;
}

class Square implements Shape {
    w: number;
    constructor(w: number) {
        this.w = w;
    }
    printType(): void {
        console.log('Square');
    }
    getArea(): number {
        return this.w * this.w;
    }

}

class Rectangle implements Shape {
    w: number;
    l: number;
    constructor(l: number, w: number) {
        this.w = w;
        this.l = l;
    }
    getArea(): number {
        return this.w * this.l;
    }
    printType(): void {
        console.log('Rectangle');
    }

}

const printArea = (shape: Shape) => {
    console.log("Area of provided shape(%s) is %s", shape.printType(), shape.getArea());
};

printArea(new Square(40));
printArea(new Rectangle(20, 45));