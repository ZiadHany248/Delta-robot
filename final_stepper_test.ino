
// Defining pins in use
short stepperStep1 = 11;
short stepperStep2 = 10;
short stepperStep3 = 9;
short stepperDir1 = 8;
short stepperDir2 = 7;
short stepperDir3 = 5;

// Variables to hold steps numbers
 int nbStepsM1 = 0;
 int nbStepsM2 = 0;
 int nbStepsM3 = 0;
 int totalStepsM1 = 0;
 int totalStepsM2 = 0;
 int totalStepsM3 = 0;

//buffers
 int currentM1 = 0; int currentM2 = 0; int currentM3 = 0; int i = 0;
int whileSig = 0;
void setup() {
  
  Serial.begin(115200);
  Serial.println("Serial is open");
  pinMode(stepperStep1, OUTPUT);
  pinMode(stepperStep2, OUTPUT);
  pinMode(stepperStep3, OUTPUT);
  pinMode(stepperDir1, OUTPUT);
  pinMode(stepperDir2, OUTPUT);
  pinMode(stepperDir3, OUTPUT);


}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available() == 0){}
  i = Serial.readString().toInt();
  
  whileSig = max(nbStepsM1, nbStepsM2);
  whileSig = max(whileSig, nbStepsM3);
  
  for(i = 0; i < whileSig; i++){

    if(currentM1 < nbStepsM1){digitalWrite(stepperStep1, HIGH);delay(30);digitalWrite(stepperStep2, LOW);currentM1++;}
    if(currentM2 < nbStepsM2){digitalWrite(stepperStep2, HIGH);delay(30);digitalWrite(stepperStep2, LOW);currentM2++;}
    if(currentM3 < nbStepsM3){digitalWrite(stepperStep3, HIGH);delay(30);digitalWrite(stepperStep3, LOW);currentM3++;}
    
                               }

  totalStepsM1  = totalStepsM1 + nbStepsM1;
  totalStepsM2  = totalStepsM2 + nbStepsM2;
  totalStepsM3  = totalStepsM3 + nbStepsM3;  
            
            }
