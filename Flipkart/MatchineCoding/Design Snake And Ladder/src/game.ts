import { Board } from "./board";
import { Dice } from "./dice";
import { Player } from "./player";

let prompt1 = require('prompt-sync')({ sigint: true });

export class Game {
    // Get user input
    isGameEnded: boolean = false;
    players: Player[] = [];
    winner: Player[] = [];

    totalDice = 1;
    dice: Dice;
    board: Board;
    boardSize = 100;
    constructor() {
        this.init();
        this.dice = new Dice();

    }
    init() {
        let noOfSnakes = Number(prompt1('Number of snakes? '));
        this.board = new Board(this.boardSize);

        for (let i = 0; i < noOfSnakes; i++) {
            let [sankeStartPos, snakeEndPos] = prompt1('Enter sankeStartPos snakeEndPos ').split(' ');

            sankeStartPos = Number(sankeStartPos);
            snakeEndPos = Number(snakeEndPos);
            console.log(sankeStartPos, typeof sankeStartPos);
            console.log(snakeEndPos, typeof snakeEndPos);
            if (sankeStartPos <= snakeEndPos) {
                console.log('snake start pos must be greater then the snake end pos ');
                break;
            }

            this.board.addSnakes(sankeStartPos, snakeEndPos);

        }

        let noOfLadder = Number(prompt1('Number of ladder? '));

        for (let i = 0; i < noOfLadder; i++) {
            let [ladderStartPos, ladderEndPos] = prompt1('Enter ladderStartPos ladderEndPos ').split(' ');
            ladderStartPos = Number(ladderStartPos);
            ladderEndPos = Number(ladderEndPos);

            if (ladderStartPos >= ladderEndPos) {
                console.log('ladder start pos must be smaller then the ladder end pos ');
                break;
            }

            this.board.addLadder(ladderStartPos, ladderEndPos);
        }
        // TODO: remove infinity loop : do we need to handle it?
        let noOfPlayer = Number(prompt1('Number of players? '));


        for (let i = 0; i < noOfPlayer; i++) {
            const playerName = prompt1('Enter Player name ').split(' ');
            this.players.push(new Player(playerName));
        }

    }

    startGame() {
        if (this.players.length == 0) {
            console.log(`can't start a game with 0 players `);
            return false;
        }
        let playerTurn = 0;
        while (this.isGameRunning()) {
            // Roll a dice for each player

            let player = this.players[playerTurn];

            let moves = this.dice.getTotalMoves(this.totalDice);
            let startPos = player.getCurrentPos();

            let posAfterMoves = startPos + moves;

            let finalPos = this.board.getFinalPos(posAfterMoves);

            if (finalPos <= this.board.getBoardSize()) {
                player.setCurrentPos(finalPos);
                player.move(startPos, finalPos);
            }
            else {
                console.log('Beeter luck next time');
            }

            if (finalPos == this.board.getBoardSize()) {
                this.winner.push(player);
            }

            if (this.shouldEndGame()) {
                this.endGame();
                this.declareResult();
            }

            playerTurn = (playerTurn + 1) % this.players.length;
        }

    }
    declareResult() {
        for (let i = 1; i <= this.winner.length; i++) {
            console.log(`${ i } Position::${ this.winner[i - 1].name }`);
        }
    }
    shouldEndGame() {
        return (this.players.length == 1 && this.winner.length == 1) || this.players.length > 1 && this.winner.length == this.players.length - 1;
    }

    endGame() {
        this.isGameEnded = true;
    }

    isGameRunning() {
        return !this.isGameEnded;
    }

}




