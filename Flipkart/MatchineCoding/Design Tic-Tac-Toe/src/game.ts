import { Player } from "./player";

export class Game {

    private board: string[][];
    private pieces: string[];
    private turn: number;
    private totalMoves: number = 0;
    private boardSize: number;

    private winner: Player[]; // multiple winners
    private players: Player[];
    private isGameOver: boolean;

    public isIsGameOver(): boolean {
        return this.isGameOver;
    }

    private setIsGameOver(isGameOver: boolean): void {
        this.isGameOver = isGameOver;
    }


    constructor(boardSize: number, pieces: string[], players: Player[]) {
        this.boardSize = boardSize;
        this.pieces = pieces;
        this.players = players;
        this.init();
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

        this.winner = [];
    }

    public getPlayers(): Player[] {
        return this.players;
    }

    public setPlayers(players: Player[]): void {
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

    isValidMove(row: number, col: number) {
        return (this.board[row][col] == '-');
    }

    makeMove(rowPos: number, colPos: number) {
        if (this.isValidMove(rowPos, colPos)) {
            this.totalMoves += 1;
            const turn = this.turn;
            this.board[rowPos][colPos] = this.getPieces()[this.turn];
            const player = this.players[this.turn];

            this.printBoard();
            this.setTurn((turn + 1) % this.players.length);
            if (this.isWinner(this.getPieces()[turn])) {
                this.winner.push(player);
                console.log(`${ player.getName() } won the game`);
            } else {

                if (this.isGameEndConditionMet()) {
                    console.log(`Game Over`);
                    this.setIsGameOver(true);
                }
            }


        } else {
            console.log('Invalid Move');
        }
    }
    isGameEndConditionMet() {
        return this.totalMoves == this.boardSize ** 2;
    }
    isWinner(piece: string): boolean {

        // Check row
        for (let row = 0; row < this.boardSize; row++) {
            let isBingo = true;
            for (let col = 0; col < this.boardSize; col++) {
                if (this.board[row][col] != piece) {
                    isBingo = false;
                    break;
                };
            }

            if (isBingo) return true;
        }

        // Check col

        for (let col = 0; col < this.boardSize; col++) {
            let isBingo = true;
            for (let row = 0; row < this.boardSize; row++) {
                if (this.board[row][col] != piece) {
                    isBingo = false;
                    break;
                };
            }

            if (isBingo) return true;
        }


        // Check diagonals
        let isBingo = true;
        for (let i = 0; i < this.boardSize; i++) {
            if (this.board[i][i] != piece) {
                isBingo = false;
                break;
            }

        }

        if (isBingo) return true;

        isBingo = true;
        for (let i = 0; i < this.boardSize; i++) {
            if (this.board[i][this.boardSize - i - 1] != piece) {
                isBingo = false;
                break;
            }
        }

        if (isBingo) return true;

        return false;
    }
    shouldGameEnd(): boolean {
        return true;
    }

    public getBoardSize(): number {
        return this.boardSize;
    }

    public setBoardSize(boardSize: number): void {
        this.boardSize = boardSize;
    }
    public getBoard(): string[][] {
        return this.board;
    }

    public setBoard(board: [string[]]): void {
        this.board = board;
    }

    public getPieces(): string[] {
        return this.pieces;
    }

    public setPieces(pieces: string[]): void {
        this.pieces = pieces;
    }

    public getTurn(): number {
        return this.turn;
    }

    public setTurn(turn: number): void {
        this.turn = turn;
    }
}