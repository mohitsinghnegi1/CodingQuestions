// Easy to extend

interface QuestionFormat {
    printDescription(): void;
    printOptions(): void;
    getAnswer(): any;


}

class MCQ implements QuestionFormat {
    description: string;
    options: string[];
    ans: number;
    constructor(desc: string, options: string[], ans: number) {
        this.description = desc;
        this.options = options;
        this.ans = ans;
    };

    printDescription() {
        console.log(this.description);
    }
    printOptions() {
        this.options.forEach((option, i) => {
            console.log(`${ i + 1 }) ${ option }`);
        });
    }
    getAnswer() {
        return this.ans;
    }
}

class FillInTheBlanks implements QuestionFormat {
    description: string;
    ans: any;

    constructor(desc: string, ans: string) {
        this.description = desc;
        this.ans = ans;
    }
    printDescription(): void {
        console.log(this.description);
    }
    printOptions(): void {
        console.log('Answer)_____________________');
    }
    getAnswer() {
        return this.ans;
    }
}




let questions = [
    new MCQ('What is earth?', ['planet', 'moon', 'sun'], 1),
    new MCQ('Who is PrimeMinister of India', ['planet', 'Modi', 'sun'], 2),
    new FillInTheBlanks('He is', 'smart')
];



// logic


const printQuestionaries = (questions: QuestionFormat[]) => {
    questions.forEach(qus => {
        qus.printDescription();
        qus.printOptions();
        console.log('correct ans is : ', qus.getAnswer());
    });
};

printQuestionaries(questions);