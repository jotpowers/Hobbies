/*

Combining photo resistor and rgb
Uses the standard libraries.  Here I was trying to understand how to compensate for the "jitter" that happened, likely due to oscillator and clock speed, and how I could compensate for it.

Yes, all of this code is ugly and poorly documented.  Welcome to hobbies.  

*/

//PhotoResistor Pin
int lightPin = 0; //the analog pin the photoresistor is
int lightPin2 = 1;  // Second photo resistor
                  
// LED leads connected to PWM pins
const int RED_LED_PIN = 9;
const int GREEN_LED_PIN = 10;
const int BLUE_LED_PIN = 11;
// 
const int ccRED_LED_PIN = 7;
const int ccGREEN_LED_PIN = 6;
const int ccBLUE_LED_PIN = 5;

const int OFF = 255;
const int JITTER = 4;
const int INTENSITY_SPACE = 15;

// Used to store the current intensity level of the individual LEDs
int redIntensity = 255;
int greenIntensity = 255;
int blueIntensity = 255;
int ccRed=0;
int ccGreen=0;
int ccBlue=20;
int result = 0;

// Length of time we spend showing each color
const int DISPLAY_TIME = 100; // In milliseconds
const int READ_HOLD_TIME = 1000; 

void setup() {
 Serial.begin(250000);  // setup the serial port
 randomSeed(analogRead(3));
// analogWrite(RED_LED_PIN, OFF);
// analogWrite(GREEN_LED_PIN, OFF);
// analogWrite(BLUE_LED_PIN, OFF);
// analogWrite(ccRED_LED_PIN, 150);
//delay(READ_HOLD_TIME);
}

void loop() {

// I want to see if we can catch pulses and distinguish between the 3 pairs

int lightLevel = analogRead(lightPin); 
int blevel = analogRead(lightPin); 
int lightLevel2 = analogRead(lightPin2);
//Serial.print("Ambient: ");
//Serial.println(lightLevel);  
//Serial.print("Ambient 2: ");
//println(lightLevel2);

//Serial.println("lightlevel ,red ,green ,blue");  

turnoff(READ_HOLD_TIME);

//clear_cycle();

int ambient = analogRead(lightPin);
int ambient2 = analogRead(lightPin2);

code(72,151,113,28);


turnoff(READ_HOLD_TIME);
exit(0);

// old code kept just to keep track of
//slope(RED_LED_PIN,DISPLAY_TIME,ambient,ambient2);
//slope(ccRED_LED_PIN,DISPLAY_TIME,ambient,ambient2);
//slope(GREEN_LED_PIN,DISPLAY_TIME,ambient,ambient2);
//slope(BLUE_LED_PIN,DISPLAY_TIME,ambient,ambient2);
//slope(ccRED_LED_PIN,100,ambient,ambient2);

//check_rgb(125,DISPLAY_TIME);
//code(72,151,113);
//code(188,22,152);

// Create a demo showing random colors and times
//for (int y=0;y<=10;y++) {
//  codeSeries(random(0,255),random(0,255),random(0,255));
//}

  
} // end loop

// let's see if we can figure out an oscilation cycle to clean out the noise
void clear_cycle() {

  char buffer[32];
  
  // blank everything out
  turnoff(READ_HOLD_TIME);
  analogWrite(RED_LED_PIN, 0);
  delay(READ_HOLD_TIME);

  Serial.println("a , b , resistor");
// Nested 
  for(int a=0;a<=100;a++) {
      for (int b=0;b<=100;b++) {
        delay(b);
         sprintf(buffer,"%d , %d , %d\n",a,b,analogRead(lightPin));
         Serial.print(buffer);
      }
      delay(a);
  }
  return;
}

// Lights up the RGB and reads the value.  The last value is the time in ms for the whole cycle
int light_and_read(int red, int green, int blue, int mstime) {
  int photoread = 0;
  int halftime = mstime/2; // split the time so we wait half, turn it on and read, wait half

  // blank everything out
  turnoff(READ_HOLD_TIME);

  delay(halftime);
  analogWrite(RED_LED_PIN, red);
  analogWrite(GREEN_LED_PIN, green);
  analogWrite(BLUE_LED_PIN, blue);
  photoread = analogRead(lightPin);
  delay(halftime);
  
  return photoread; // returns the value from the read
}

// just turn the whole thing off
void turnoff(int time) {
  analogWrite(RED_LED_PIN, OFF);
  analogWrite(GREEN_LED_PIN, OFF);
  analogWrite(BLUE_LED_PIN, OFF);
  delay(time);
  return;
}

// let's create dummy code blocks
void code (int red,int green,int blue,int jitter) {

  char buffer[32];

  //sprintf(buffer,"Code one for %d , %d , %d, %d\n",red,green,blue,jitter);
  //Serial.print(buffer);

  turnoff(READ_HOLD_TIME);
  int halftime = READ_HOLD_TIME/2; // split the time so we wait half, turn it on and read, wait half

  // turn every thing on
  analogWrite(RED_LED_PIN, red);
  analogWrite(GREEN_LED_PIN, green);
  analogWrite(BLUE_LED_PIN, blue);
  delay(halftime);  // pause

  // now read as fast as we can with a jitter delay to deal with oscillation 
  for(int x=0;x<=10;x++) {
  int photoread = analogRead(lightPin);
  int photoread2 = analogRead(lightPin2);
  delay(jitter);
  sprintf(buffer,"%d , %d , %d\n",photoread,photoread2,jitter);
  Serial.print(buffer);
  }// end for
  
  delay(halftime);
return;
}

void codeSeries (int red,int green,int blue) {

  char buffer[32];

  sprintf(buffer,"%d , %d , %d , ",red,green,blue);
  Serial.print(buffer);
    
  turnoff(READ_HOLD_TIME);
 // int halftime = READ_HOLD_TIME/2; // split the time so we wait half, turn it on and read, wait half
  //int halftime = random(30,300); // just for demo
  analogWrite(RED_LED_PIN, red);
  analogWrite(GREEN_LED_PIN, green);
  analogWrite(BLUE_LED_PIN, blue);
  delay(halftime);
  int photoread = analogRead(lightPin);
  int photoread2 = analogRead(lightPin2);
  delay(halftime);

  Serial.print(photoread);
  Serial.print(" ,");
  Serial.println(photoread2);

return;
}

int check_rgb (int intensity, int mstime) {
  turnoff(READ_HOLD_TIME);

  result = light_and_read(intensity,intensity,0,mstime);
  Serial.print("Red/blue, ");
  Serial.println(result);

  turnoff(READ_HOLD_TIME);

  result = light_and_read(intensity,0,intensity,mstime);
  Serial.print("Red/green, ");
  Serial.println(result);

  turnoff(READ_HOLD_TIME);

  result = light_and_read(0,intensity,intensity,mstime);
  Serial.print("blue/green, ");
  Serial.println(result);

return 0;
}

// Cycle through every increment from lights to dimmest
void slope (int pin,int mdelay,int ambient,int ambient2) {

  int result = -666;
  int result2 = -555;

  for(int x = 255;x>=0;x-=INTENSITY_SPACE) {
    analogWrite(pin,x);
    delay(mdelay); // wait to allow light to turn on
    if (JITTER != 0) { print_jitter(ambient); }
    result = analogRead(lightPin);
    result2 = analogRead(lightPin2);
    turnoff(mdelay); // wait to keep the light on
    int delta = result - result2; // let's see if the delta between these is interesting
   // result -= ambient;
   // result2 -= ambient2;
    // Here we
    Serial.print(x);
    Serial.print(" ,");
    Serial.print(result);
    Serial.print(" ,");
    Serial.print(result2);
    Serial.print(" ,");
    Serial.println(delta);
  }
  return;
}

void print_jitter(int off) {
    Serial.println("Starting jitter test");
    for(int x=0;x<100;x++) {
      result = analogRead(lightPin);
      result -= off;
      Serial.print(x); Serial.print(" ,");
      Serial.println(result);
      delay(25);
    } // end jitter test
    Serial.println("Ending jitter test");
}
