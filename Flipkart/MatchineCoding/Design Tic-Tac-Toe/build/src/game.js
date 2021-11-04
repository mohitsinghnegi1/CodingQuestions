"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Game = void 0;
class Game {
    constructor(boardSize, pieces, players) {
        this.totalMoves = 0;
        this.boardSize = boardSize;
        this.pieces = pieces;
        this.players = players;
        this.init();
    }
    isIsGameOver() {
        return this.isGameOver;
    }
    setIsGameOver(isGameOver) {
        this.isGameOver = isGameOver;
    }
    init() {
        //    Board
        this.board = [];
        for (let i = 0; i < this.getBoardSize(); i++) {
            let row = [];
            for (let j = 0; j < this.getBoardSize(); j++) {
                row.push('-');
            }
            this.board.push(row);
        }
        this.printBoard();
        // pieces ie set by user
        this.setTurn(0);
    }
    getPlayers() {
        return this.players;
    }
    setPlayers(players) {
        this.players = players;
    }
    printBoard() {
        const board = this.getBoard();
        for (let i = 0; i < this.getBoardSize(); i++) {
            let row = " ";
            for (let j = 0; j < this.getBoardSize(); j++) {
                row += board[i][j] + ' ';
            }
            console.log(row);
        }
        console.log();
    }
    isValidMove() {
        return true; // TODO
    }
    makeMove(rowPos, colPos) {
        if (this.isValidMove()) {
            this.turn = this.turn;
            this.board[rowPos][colPos] = this.getPieces()[this.turn];
            const player = this.players[this.turn];
            this.printBoard();
            if (this.isWinner(this.getPieces()[this.turn])) {
                this.winner.push(player);
                console.log(`${player.getName()} won the game`);
            }
            else {
                if (this.isGameEndConditionMet()) {
                    console.log(`Game Over`);
                    this.setIsGameOver(true);
                }
            }
            this.setTurn((this.turn + 1) % this.players.length);
            this.totalMoves += 1;
        }
        else {
            console.log('Invalid Move');
        }
    }
    isGameEndConditionMet() {
        return this.totalMoves == this.boardSize ** 2;
    }
    isWinner(piece) {
        // Check row
        for (let row = 0; row < this.boardSize; row++) {
            let isBingo = true;
            for (let col = 0; col < this.boardSize; col++) {
                if (this.board[row][col] != piece) {
                    isBingo = false;
                    break;
                }
                ;
            }
            if (isBingo)
                return true;
        }
        // Check col
        for (let col = 0; col < this.boardSize; col++) {
            let isBingo = true;
            for (let row = 0; row < this.boardSize; row++) {
                if (this.board[row][col] != piece) {
                    isBingo = false;
                    break;
                }
                ;
            }
            if (isBingo)
                return true;
        }
        // Check diagonals
        let isBingo = true;
        for (let i = 0; i < this.boardSize; i++) {
            if (this.board[i][i] != piece) {
                isBingo = false;
                break;
            }
        }
        if (isBingo)
            return true;
        isBingo = true;
        for (let i = 0; i < this.boardSize; i++) {
            if (this.board[i][this.boardSize - i - 1] != piece) {
                isBingo = false;
                break;
            }
        }
        if (isBingo)
            return true;
        return false;
    }
    shouldGameEnd() {
        return true;
    }
    getBoardSize() {
        return this.boardSize;
    }
    setBoardSize(boardSize) {
        this.boardSize = boardSize;
    }
    getBoard() {
        return this.board;
    }
    setBoard(board) {
        this.board = board;
    }
    getPieces() {
        return this.pieces;
    }
    setPieces(pieces) {
        this.pieces = pieces;
    }
    getTurn() {
        return this.turn;
    }
    setTurn(turn) {
        this.turn = turn;
    }
}
exports.Game = Game;
//# sourceMappingURL=game.js.map