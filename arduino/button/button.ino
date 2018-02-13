const int buttonPin0 =A0;
int buttonState0 = 0;
int8_t isk1_stoped = 0;
int8_t i1 = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(buttonPin0, INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  buttonState0 = digitalRead(buttonPin0);
   if(buttonState0 == LOW) 
  { 
    isk1_stoped=1;// 检查按键是否被按下 
    i1=2;
  }
  else{
    isk1_stoped=0;// 检查按键是否被按下 
    i1=1;
  }
  
  int z = i1;
   //int z = 1000+i*100+j*10+k;
   char string[25];
   itoa(z, string, 10);
   delay(1000);
   Serial.write(string);
}
