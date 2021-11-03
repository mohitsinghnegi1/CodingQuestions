
export class Dice {

    maxSixCount = 3;

    private rollDice() {
        return Math.floor(Math.random() * 10 + 1);
    }

    getTotalMoves(noofDice: number) {
        let moves = 0;

        for (let i = 0; i < noofDice; i++) {
            let no = this.rollDice();

            let sixCount = 0;
            while (no == 6 && sixCount < 3) {
                sixCount += 1;

                if (sixCount == this.maxSixCount) {
                    sixCount = 0;
                    break;
                }
                no = this.rollDice() + sixCount * 6;
            }
            moves += no;
        }
        return moves;
    }

}