export class Player {
    currentPos: number;
    name: string;
    constructor(name: string) {
        this.currentPos = 0;
        this.name = name;
    }

    getCurrentPos() {
        return this.currentPos;
    }

    setCurrentPos(pos: number) {
        this.currentPos = pos;
    }

    move(start: number, end: number) {
        console.log(` rolled a ${ this.name } and moved from ${ start } to ${ end }`);
    }
    reset() {
        this.currentPos = 0;
    }

}