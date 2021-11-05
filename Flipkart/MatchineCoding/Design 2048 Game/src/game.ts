import { IGame } from "../interfaces/Igames";
import { Board } from "./board";
let prompt1 = require('prompt-sync')({ sigint: true });
export class Game implements IGame {
    board: Board;

    constructor() {
        this.init();
    }
    init(): void {
        this.board = new Board(4, 4);
    }
    playGame(): void {
        console.log(`press \n 0 denotes left \n 1 denotes right \n  2 denotes top \n 3 denotes bottom \n`);
        while (true) {
            const direction = Number(prompt1());
            this.board.move(direction);
        }
    }
};;