int X1pin = A1, Y1pin = A0, X2pin = A3, Y2pin = A2, S1pin = 2, S2pin = 3, dt = 0;
int X1val, Y1val, S1val, X2val, Y2val, S2val;
char userInput;

void setup() {
	// put your setup code here, to run once:
	Serial.begin(115200);
	pinMode(X1pin, INPUT);
	pinMode(Y1pin, INPUT);
	pinMode(S1pin, INPUT);
    pinMode(X2pin, INPUT);
	pinMode(Y2pin, INPUT);
	pinMode(S2pin, INPUT);
	digitalWrite(S1pin, 1);
	digitalWrite(S2pin, 1);
}

int* printJoystickVal() {
	X1val = analogRead(X1pin);
	Y1val = analogRead(Y1pin);
	S1val = digitalRead(S1pin);
	
    X2val = analogRead(X2pin);
    Y2val = analogRead(Y2pin);
	S2val = digitalRead(S2pin);
	
	delay(dt);
    Serial.print(X1val);
    Serial.print(",");
    Serial.print(Y1val);
    Serial.print(",");
    Serial.print(S1val);
    Serial.print(",");
    Serial.print(X2val);
    Serial.print(",");
    Serial.print(Y2val);
    Serial.print(",");
    Serial.println(S2val);
}

void loop() {
	// put your main code here, to run repeatedly:
	if(Serial.available() > 0) {
		userInput = Serial.read();		
		if(userInput == 'y') {
            printJoystickVal();
		}
	}
}