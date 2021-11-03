
export class Board {
    size: number;
    board: Object = {};

    constructor(size: number) {
        this.size = size;
    }


    private isValidPos(startPos: number, endPos: number) {
        if (startPos >= 100 || endPos > 100) return false;
        return true;
    }

    addSnakes(startPos: number, endPos: number): boolean {

        if (this.isValidPos(startPos, endPos)) return false;

        this.board[startPos] = { endPos: Number, type: 'snake' };
        return true;
    }

    addLadder(startPos: number, endPos: number): boolean {
        if (this.isValidPos(startPos, endPos)) return false;
        this.board[startPos] = { endPos: Number, type: 'ladder' };
        return true;
    }

    isCurrentPosHasSnakeOrLadder(pos: number) {
        return this.board.hasOwnProperty(pos);
    }

    getFinalPos(pos: number) {
        if (this.isCurrentPosHasSnakeOrLadder(pos)) {
            return this.board[pos].end;
        }
        return pos;
    }

    getBoardSize() {
        return this.size;
    }

}