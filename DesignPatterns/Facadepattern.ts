// Hiding the complexity inside a single function of a  class
// The facade pattern is a software-design pattern commonly used in object-oriented programming. Analogous to a facade in architecture, 
// a facade is an object that serves as a front-facing interface masking more complex underlying or structural code.


class PopCornMaker {
    turnOn() {
        console.log('Turned on pop corn maker');
    }
    turnOff() {
        console.log('Turn off pop corn maker');
    }

    pop() {
        console.log('Pop the corn');
    }
}

class Light {
    dim() {
        console.log('Dim the light');
    }
    bright() {
        console.log('Bright the light');
    }
}

class TV {
    turnOn() {
        console.log('Turn on the tv');
    }
    turnOff() {
        console.log('Turn off the tv');
    }
}

class HomeThreater {
    popCornMaker: PopCornMaker;
    light: Light;
    tv: TV;

    constructor(popCornMaker: PopCornMaker, light: Light, tv: TV) {
        this.popCornMaker = popCornMaker;
        this.light = light;
        this.tv = tv;
    }
    watchMovie() {
        this.popCornMaker.turnOn();
        this.popCornMaker.pop();
        this.popCornMaker.turnOff();

        this.light.dim();

        this.tv.turnOn();
        console.log('Watching movie');
    }
    endMovie() {
        console.log('Ending Movie');
        this.light.bright();
        this.tv.turnOff();
    }
}

let popCornMaker = new PopCornMaker();
let tv = new TV();
let light = new Light();
let homeThreater = new HomeThreater(popCornMaker, light, tv);
homeThreater.watchMovie();
homeThreater.endMovie();