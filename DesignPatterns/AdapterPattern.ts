interface ILightningToMicroUsbPortAdapter {
    useMicroUsBPort(iphone: IPhoneInteface): void;
}


interface Android {
    useMicroUsBPort(): void;
}

interface IPhoneInteface {
    useLisghtningPort(): void;
}

class IPhone7 implements IPhoneInteface {
    useLisghtningPort(): void {
        console.log('Using Lightning Port');
    }
}

class GooglePixel implements Android {
    useMicroUsBPort(): void {
        console.log('Using Micro USB port');
    }

}

class LightningToMicroUSBAdapter implements ILightningToMicroUsbPortAdapter {
    useMicroUsBPort(iphone: IPhoneInteface): void {
        console.log('Using Adapter to  convert Lightning port to MicroUsb port');
        iphone.useLisghtningPort();
    }

}


let iphone7 = new IPhone7();
// i have Lightning Port
// I need an adapter which convert lightning to microUSB
let adapter = new LightningToMicroUSBAdapter();
adapter.useMicroUsBPort(iphone7);