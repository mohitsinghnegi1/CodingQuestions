import { IBoard } from "../interfaces/Iboard";
import { DIRECTION } from "../types/direction";

export class Board implements IBoard {
    board: number[][];
    isEnd: boolean;
    isWinner: boolean;
    rows: number;
    cols: number;
    winningNumber: number;

    constructor(rows: number, cols: number) {
        this.cols = cols;
        this.rows = rows;
        this.init();
    }
    init(): void {
        this.isWinner = false;
        this.isEnd = false;
        this.winningNumber = 32;
        this.initBoard();
        this.insertRandomTile();
        this.insertRandomTile();
        this.printBoard();
    }

    initBoard() {
        this.board = [];
        for (let i = 0; i < this.rows; i++) {
            let row = [];
            for (let j = 0; j < this.cols; j++) {
                row.push(0);
            }
            this.board.push(row);
        }

    }
    printBoard(): void {

        for (let i = 0; i < this.rows; i++) {
            let row = ' ';
            for (let j = 0; j < this.cols; j++) {
                row += this.board[i][j] + ' ';
            }
            console.log(row);
        }
        console.log();
    }
    move(direction: DIRECTION): void {
        this.slide(direction);
        let canCombine = this.perocessCombine(direction);
        let isSlideHappend = this.slide(direction);

        if (isSlideHappend)
            this.insertRandomTile();
        console.log("here");
        this.printBoard();
        if (this.isWinner) {
            console.log('Congratulations');
            process.exit();

        }

        console.log("this.checkGameEndCondition(canCombine)", this.checkGameEndCondition(canCombine));
        if (this.checkGameEndCondition(canCombine)) {
            this.endGame();
            console.log('Game Over');
            process.exit();
        }
    }
    checkGameEndCondition(canCombine: boolean): boolean {
        console.log("!canCombine", !canCombine);
        console.log("this.isAllCellFilled()", this.isAllCellFilled());
        return !canCombine && this.isAllCellFilled();
    }
    isAllCellFilled(): boolean {
        for (let i = 0; i < this.rows; i++) {

            for (let j = 0; j < this.cols; j++) {
                if (this.board[i][j] == 0)
                    return false;
            }

        }
        return true;
    }

    slideLeft() {
        let isSlideHappend = false;

        for (let i = 0; i < this.rows; i++) {

            let isMoved = this.moveZeroes(this.board[i]);
            if (isMoved) {
                isSlideHappend = true;
            }
        }



        return isSlideHappend;
    }

    swap(arr: number[], i: number, j: number) {
        let temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    moveZeroes(arr: number[]) {
        let isMoved = false;


        let insertPos = 0;
        let lastPos = 0;

        for (let i = 0; i < arr.length; i++) {
            if (arr[i] != 0) {
                lastPos = i;
                this.swap(arr, i, insertPos);
                insertPos += 1;
            }
        }

        if (lastPos != insertPos) {
            isMoved = true;
        }

        return isMoved;
    }

    slideTop() {
        let isSlideHappend = false;

        for (let col = 0; col < this.cols; col++) {
            let insertPos = 0;
            let lastPos = 0;
            for (let row = 0; row < this.rows; row++) {
                if (this.board[row][col] != 0) {
                    lastPos = row;

                    // swap 
                    let temp = this.board[insertPos][col];
                    this.board[insertPos][col] = this.board[row][col];
                    this.board[row][col] = temp;

                    insertPos += 1;
                }
            }

            if (lastPos != insertPos) {
                isSlideHappend = true;
            }

        }

        return isSlideHappend;
    }


    slide(direction: DIRECTION): boolean {
        let isSlideHappend = false;

        switch (direction) {
            case DIRECTION.LEFT:
                isSlideHappend = this.slideLeft();

                break;

            case DIRECTION.RIGHT:
                this.reverseCols(this.board);
                isSlideHappend = this.slideLeft();
                this.reverseCols(this.board);

                break;

            case DIRECTION.TOP:

                isSlideHappend = this.slideTop();

                break;

            case DIRECTION.BOTTOM:
                this.board.reverse();
                isSlideHappend = this.slideTop();
                this.board.reverse();

                break;
        }

        console.log("after slide ");
        this.printBoard();

        return isSlideHappend;
    }

    combineRight() {
        let canCombine = false;
        for (let i = 0; i < this.rows; i++) {
            let j = 1;
            while (j < this.cols) {
                if (this.board[i][j] != 0 && this.board[i][j - 1] == this.board[i][j]) {
                    console.log("horay");
                    this.board[i][j] = this.board[i][j] * 2;
                    this.board[i][j - 1] = 0;
                    if (this.board[i][j] == this.winningNumber) this.isWinner = true;
                    canCombine = true;
                    j += 2;
                } else
                    j += 1;
            }
        }
        return canCombine;
    }
    combineTop() {
        let canCombine = false;
        for (let j = 0; j < this.cols; j++) {
            let i = 1;
            while (i < this.cols) {
                if (this.board[i - 1][j] == this.board[i][j]) {
                    this.board[i][j] = this.board[i][j] * 2;
                    this.board[i - 1][j] = 0;
                    if (this.board[i][j] == this.winningNumber) this.isWinner = true;
                    i += 2;
                    canCombine = true;
                } else
                    i += 1;

            }
        }
        return canCombine;
    }

    reverseCols(board: number[][]) {
        for (let i = 0; i < board.length; i++) {
            board[i].reverse();
        }
    }

    perocessCombine(direction: DIRECTION): boolean {


        let canCombine = false;

        switch (direction) {
            case DIRECTION.LEFT:
                this.reverseCols(this.board);


                canCombine = this.combineRight();

                this.reverseCols(this.board);


                break;

            case DIRECTION.RIGHT:
                canCombine = this.combineRight();
                break;

            case DIRECTION.TOP:

                canCombine = this.combineTop();
                break;

            case DIRECTION.BOTTOM:
                this.board.reverse();
                canCombine = this.combineTop();
                this.board.reverse();
                break;
            default:
                console.log("invalid direction");
        }

        console.log("after combine");
        this.printBoard();

        return canCombine;
    }

    isGameEnd(): boolean {
        return this.isEnd;
    }
    insertRandomTile(): boolean {
        const freeTiles = this.getFreeTiles();
        if (freeTiles.length == 0) return false;

        const randomTile = this.getRandomTile(freeTiles);
        console.log("random Tile", randomTile, randomTile == []);
        if (randomTile.length == 0) return false;
        this.board[randomTile[0]][randomTile[1]] = this.getRandomNumber();

        return true;
    }
    getRandomNumber(): number {
        return Math.random() > 0.5 ? 2 : 4;
    }

    getRandomTile(tiles: number[][]): number[] {
        if (tiles.length == 0) {
            console.log("getRandomTile::tile list is Empty");
            return [];
        };
        let randomIndex = Math.floor(Math.random() * 10) % tiles.length;
        return tiles[randomIndex];
    }

    getFreeTiles() {
        let freeTiles: number[][] = [];

        for (let i = 0; i < this.rows; i++) {

            for (let j = 0; j < this.cols; j++) {
                if (this.board[i][j] == 0) {
                    freeTiles.push([i, j]);
                }
            }
        }
        return freeTiles;
    }

    endGame() {
        this.isEnd = true;
    }
    getRows(): number {
        return this.rows;
    }
    getCols(): number {
        return this.cols;
    }

}


