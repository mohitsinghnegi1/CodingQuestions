import { DIRECTION } from "../types/direction";

export interface IBoard {

    board: number[][];
    isEnd: boolean;
    isWinner: boolean;
    rows: number;
    cols: number;
    init(): void;

    move(direction: DIRECTION);
    slide(direction: DIRECTION): boolean;
    perocessCombine(direction: DIRECTION): boolean; // Also isWinner to true, // also set is gameEnd
    isGameEnd(): boolean;
    insertRandomTile(): boolean;
    getRows(): number;
    getCols(): number;
    printBoard(): void;
}