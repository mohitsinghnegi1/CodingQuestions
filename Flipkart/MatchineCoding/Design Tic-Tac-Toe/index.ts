import { Game } from "./src/game";
import { Player } from "./src/player";

// Stop taking input when game ends
let prompt1 = require('prompt-sync')({ sigint: true });



const size = 3;
const pieces = ['X', 'O'];
const noOfPlayers = 2;

let exit = false;
while (!exit) {
    let players: Player[] = [];
    for (let i = 0; i < noOfPlayers; i++) {
        players.push(new Player(prompt1(`${ pieces[i] } `)));
    }

    const game = new Game(size, pieces, players);

    while (!exit) {

        let input = prompt1();

        if (input == 'exit') {
            exit = true;
        } else {
            let cordinates = input.split(' ');
            game.makeMove(cordinates[0] - 1, cordinates[1] - 1);

            if (game.isIsGameOver()) {
                exit = true;
            }
        }
    }
}