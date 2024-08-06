#include<stdio.h>
int main(){
    long int hisob=1000000000;
    long int avvalgi=hisob;
    int taom_tanlov;
    start :
    printf("[1]-Milliy taomlar\n");
    printf("[2]-Fast food\n");
    printf("[3]-choy+kofe\n");
    printf("[4]-Dessertlar\n");
    printf("[5]-Hisobni bilish\n");
    int tanlov,olmoq;
    scanf("%d",&taom_tanlov);

    switch(taom_tanlov){
        case 1: 
        metka :
        printf("[1]-Osh 30000\n");
        printf("[2]-Qozon kabob 40000\n");
        printf("[3]-Norin 35000\n");
        printf("[4]-Mastava 25000\n");
        printf("[5]-Xalim 28000\n");
        printf("[6]-Bosh menyuga qaytish\n");
        scanf("%d",&tanlov);
        switch(tanlov){
            case 1:
            puts("[1]-1 portsiya 30000");
            puts("[2]-0.7 portsiya 25000");
            puts("[3]-1.5 portsiya 45000");
            puts("[4]-2 portsiya 60000 skidka bilan 50000");
            puts("[5]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1: 
                hisob=hisob-30000;
                goto metka; 
                case 2:
                hisob-=25000;
                goto metka;
                case 3:
                hisob=hisob-45000;
                goto metka;
                case 4:
                hisob-=50000;
                goto metka;
                case 5:
                goto metka;
                default : 
                puts("Xatolik");
            }   
            case 2:
            puts("[1]-1 portsiya 40000");
            puts("[2]-0.7 portsiya 35000");
            puts("[3]-1.5 portsiya 60000");
            puts("[4]-2 portsiya 80000 skidka bilan 70000");
            puts("[5]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1: 
                hisob=hisob-40000;
                goto metka; 
                case 2:
                hisob-=35000;
                goto metka;
                case 3:
                hisob=hisob-60000;
                goto metka;
                case 4:
                hisob-=70000;
                goto metka;
                case 5:
                goto metka;
                default : 
                puts("Xatolik");
            }   
            case 3:
            puts("[1]-1 portsiya 35000");
            puts("[2]-0.7 portsiya 30000");
            puts("[3]-1.5 portsiya 55000");
            puts("[4]-2 portsiya 70000 skidka bilan 60000");
            puts("[5]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1: 
                hisob=hisob-35000;
                goto metka; 
                case 2:
                hisob-=30000;
                goto metka;
                case 3:
                hisob=hisob-55000;
                goto metka;
                case 4:
                hisob-=60000;
                goto metka;
                case 5:
                goto metka;
                default : 
                puts("Xatolik");
            } 
            case 4:  
            puts("[1]-1 portsiya 25000");
            puts("[2]-0.7 portsiya 20000");
            puts("[3]-1.5 portsiya 35000");
            puts("[4]-2 portsiya 50000 skidka bilan 40000");
            puts("[5]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1: 
                hisob=hisob-25000;
                goto metka; 
                case 2:
                hisob-=20000;
                goto metka;
                case 3:
                hisob=hisob-35000;
                goto metka;
                case 4:
                hisob-=40000;
                goto metka;
                case 5:
                goto metka;
                default : 
                puts("Xatolik");
            }   
            case 5:
            puts("[1]-1 portsiya 28000");
            puts("[2]-0.7 portsiya 24000");
            puts("[3]-1.5 portsiya 42000");
            puts("[4]-2 portsiya 56000 skidka bilan 46000");
            puts("[5]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1: 
                hisob=hisob-28000;
                goto metka; 
                case 2:
                hisob-=24000;
                goto metka;
                case 3:
                hisob=hisob-42000;
                goto metka;
                case 4:
                hisob-=46000;
                goto metka;
                case 5:
                goto metka;
                default : 
                puts("Xatolik");
            }   
            case 6:
            goto start;        
        }
        case 2:
        metka1 :
        puts("[1]-Lavash");
        puts("[2]-cheezburger");
        puts("[3]-Sandwich club");
        puts("[4]-gamburger");
        puts("[5]-Bosh menyuga qaytish");
        scanf("%d",&tanlov);
        switch(tanlov){
            case 1:
            puts("[1]-Tovuqli 26000 ");
            puts("[2]-goshtli 28000");
            puts("[3]-Tovuqli mini 20000");
            puts("[4]-goshtli mini 22000");
            puts("[5]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1:
                hisob-=26000;
                goto metka1;
                case 2:
                hisob-=28000;
                goto metka1;
                case 3:
                hisob-=20000;
                goto metka1;
                case 4:
                hisob-=22000;
                goto metka1;
                case 5:
                goto metka1;
            }
            case 2:
             puts("[1]-Tovuqli 26000 ");
             puts("[2]-goshtli 30000");
             puts("[3]-Tovuqli mini 24000");
             puts("[4]-goshtli mini 26000");
             puts("[5]-ortga qaytish");
             scanf("%d",&olmoq);
             switch(olmoq){
                case 1:
                hisob-=26000;
                goto metka1;
                case 2:
                hisob-=30000;
                goto metka1;
                case 3:
                hisob-=24000;
                goto metka1;
                case 4:
                hisob-=26000;
                goto metka1;
                case 5:
                goto metka1;
            }
            case 3:
             puts("[1]-Tovuqli 28000 ");
             puts("[2]-goshtli 30000");
             puts("[3]-Ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1:
                hisob=hisob-28000;
                goto metka1;
                case 2:
                hisob-=30000;
                goto metka1;
                case 3:
                goto metka1;
            }
            case 4:
             puts("[1]-Tovuqli 24000 ");
             puts("[2]-goshtli 26000");
             puts("[3]-Tovuqli mini 22000");
             puts("[4]-goshtli mini 24000");
             puts("[5]-ortga qaytish");
             scanf("%d",&olmoq);
             switch(olmoq){
                case 1:
                hisob-=24000;
                goto metka1;
                case 2:
                hisob-=26000;
                goto metka1;
                case 3:
                hisob-=22000;
                goto metka1;
                case 4:
                hisob-=24000;
                goto metka1;
                case 5:
                goto metka1;
            }
            case 5:
            goto start;
        }   
        case 3:
        metka2:
        puts("[1]-kok choy");
        puts("[2]-qora choy");
        puts("[3]-limonli kok choy");
        puts("[4]-limonli qora choy");
        puts("[5]-kofe");
        puts("[6]-Bosh menyuga qaytish");
        scanf("%d",&tanlov);
        switch(tanlov){
            case 1:
            puts("[1]-8000");
            puts("[2]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1:
                hisob-=8000;
                goto metka2;
                case 2:
                goto metka2;
            }
            case 2:
            puts("[1]-10000");
            puts("[2]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1:
                hisob-=10000;
                goto metka2;
                case 2:
                goto metka2;
            }
            case 3:
            puts("[1]-8000");
            puts("[2]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1:
                hisob-=10000;
                goto metka2;
                case 2:
                goto metka2;
            }
            case 4:
            puts("[1]-12000");
            puts("[2]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1:
                hisob-=12000;
                goto metka2;
                case 2:
                goto metka2;
            }
            case 5:
            puts("[1] ta stakan 15000");
            puts("[2] ta stakan 20000 skidka bilan");
            puts("[3] ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1:
                hisob-=15000;
                goto metka2;
                case 2:
                hisob-=20000;
                goto metka2;
                case 3:
                goto metka2;
            } 
            case 6:
            goto start;
        }
        case 4:
        metka3:
        puts("[1]-Napoleon");
        puts("[2]-olchali pirog");
        puts("[3]-shokoladli tort");
        puts("[4]-Tvorogli pirog");
        puts("[5]-Bosh menyuga qaytish");
        scanf("%d",&tanlov);
        switch(tanlov){
            case 1:
            puts("[1] bolak 15000");
            puts("[2]-bolak 25000");
            puts("[3]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1:
                hisob-=15000;
                goto metka3;
                case 2:
                hisob-=25000;
                goto metka3;
                case 3:
                goto metka;
            }
            case 2:
             puts("[1] bolak 10000");
             puts("[2]-bolak 15000");
             puts("[3]-ortga qaytish");
             scanf("%d",&olmoq);
             switch(olmoq){
                case 1:
                hisob-=10000;
                goto metka3;
                case 2:
                hisob-=15000;
                goto metka3;
                case 3:
                goto metka;
            }
            case 3:
            puts("[1] bolak 15000");
            puts("[2]-bolak 25000");
            puts("[3]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1:
                hisob-=15000;
                goto metka3;
                case 2:
                hisob-=25000;
                goto metka3;
                case 3:
                goto metka;
            }  
            case 4:      
            puts("[1] bolak 12000");
            puts("[2]-bolak 18000");
            puts("[3]-ortga qaytish");
            scanf("%d",&olmoq);
            switch(olmoq){
                case 1:
                hisob-=12000;
                goto metka3;
                case 2:
                hisob-=18000;
                goto metka3;
                case 3:
                goto metka;
            }
            case 5:
            goto start;
        }
        case 5:
        puts("Haridingizdan minnatdormiz osh bo'lsin");
        printf("Shu  %d mablag'dan %d mablagingiz qoldi ",avvalgi,hisob);    

    }
    
}
