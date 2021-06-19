interface IInfo {
    temperature: number;
}

interface IPub {
    info: IInfo;
    registerSub(sub: ISub): boolean;
    unregisterSub(sub: ISub): boolean;
    publish(info: IInfo, subscribers: ISub[]): void;
}
interface ISub {
    info: IInfo;
    update(info: IInfo): void;
}

class WeatherStation implements IPub {
    info: IInfo = { temperature: 0 };
    subscribers: ISub[] = [];

    setInfo(info: IInfo) {
        this.info = info;
        console.log('WeatherStation:: Temperature updated ', this.info.temperature);
        console.log('WeatherStation:: Broadcasting temperature');
        this.publish(this.info, this.subscribers);
    }

    registerSub(sub: ISub): boolean {
        this.subscribers.push(sub);
        return true;
    }
    unregisterSub(sub: ISub): boolean {
        this.subscribers = this.subscribers.filter(subscriber => {
            return sub != subscriber;
        });
        return true;
    }
    publish(info: IInfo, subscribers: ISub[]): void {
        subscribers.forEach(subscriber => {
            subscriber.update(info);
        });
    }
}

class TemperatureDisplay implements ISub {
    info: IInfo = { temperature: 0 };

    weatherStation: IPub;

    constructor(weatherStation: IPub) {
        this.weatherStation = weatherStation;
        weatherStation.registerSub(this);
    }
    update(info: IInfo): void {
        this.info = info;
        console.log('Current Temperature is %s', this.info.temperature);
    }

}

class AIFan implements ISub {
    info: IInfo = { temperature: 0 };
    weatherStation: IPub;

    constructor(weatherStation: IPub) {
        this.weatherStation = weatherStation;
        weatherStation.registerSub(this);
    }

    update(info: IInfo): void {
        this.info = info;
        if (this.info.temperature < 30) {
            console.log("AIFan:: Switching off");
        } else {
            console.log("AIFan:: Switching on ");
        }
    }

}


// Create Publiser 

let weatherStation = new WeatherStation();


// Create Subscribers and subscribe
let tempDisplay = new TemperatureDisplay(weatherStation);
let aiFan = new AIFan(weatherStation);

weatherStation.setInfo({ temperature: 20 });
weatherStation.setInfo({ temperature: 30 });
