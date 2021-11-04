"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const game_1 = require("./src/game");
const player_1 = require("./src/player");
// Stop taking input when game ends
let prompt1 = require('prompt-sync')({ sigint: true });
const size = 3;
const pieces = ['X', 'O'];
const noOfPlayers = 2;
let exit = false;
while (exit) {
    let players = [];
    for (let i = 0; i < noOfPlayers; i++) {
        players.push(new player_1.Player(prompt1(`${pieces[i]} `)));
    }
    const game = new game_1.Game(size, pieces, players);
    while (exit) {
        let input = prompt1();
        if (input == 'exit') {
            exit = true;
        }
        else {
            let cordinates = input.split(' ');
            game.makeMove(cordinates[0], cordinates[1]);
            if (game.isIsGameOver()) {
                exit = true;
            }
        }
    }
}
//# sourceMappingURL=index.js.map