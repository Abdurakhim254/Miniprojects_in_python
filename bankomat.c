#include<stdio.h>
int main(){
long int hisob=100000000;
long int balans=hisob;
int parol=1234,tolov,xizmat,count=0,xizmat_tanlov;
int pin,tel,scet,summa;
puts("Iltimos kartangizni kiriting");
qaytish:
printf("Iltimos parolni tering :");
scanf("%d",&pin);
if(pin==parol){
    bosh :
    puts("Xizmat turini tanlang ");
    puts("[1]-Kommunal tolov");
    puts("[2]-Mobil aloqa vositalari boyicha tolov");
    puts("[3]-Internet+wifi");
    puts("[4]-Naqd pul yechish");
    puts("[5]-Balansni tekshirish");
    puts("[6]-Tolov mobaynida qolgan pulni tekshirish");
    scanf("%d",&xizmat_tanlov);
    switch(xizmat_tanlov){
        case 1:
        metka:
        puts("[1]-Gaz");
        puts("[2]-Elektr");
        puts("[3]-suv");
        puts("[4]-Ortga qaytish");
        scanf("%d",&xizmat);
        switch(xizmat){
            case 1:
            puts("Iltimos litsevoy scetni kiriting :");scanf("%d",&scet);
            puts("Tolov miqdorini kiriting :");
            scanf("%d",&tolov);
            hisob-=tolov;
            puts("Tolov muvafaqqiyatli amalga oshirildi");
            goto metka; 
            case 2:
            puts("Iltimos litsevoy scetni kiriting :");scanf("%d",&scet);
            puts("Tolov miqdorini kiriting :");
            scanf("%d",&tolov);
            hisob-=tolov;
            puts("Tolov muvafaqqiyatli amalga oshirildi");
            goto metka; 
            case 3:
            puts("Iltimos litsevoy scetni kiriting :");scanf("%d",&scet);
            puts("Tolov miqdorini kiriting :");
            scanf("%d",&tolov);
            hisob-=tolov;
            puts("Tolov muvafaqqiyatli amalga oshirildi");
            goto metka; 
            case 4:
            goto bosh;
            default :
            puts("Xizmat tanlashda xatolik");
            goto metka;
        
        }
        case 2:
        metka1:
        puts("[1]-Uzmobile");
        puts("[2]-Beeline");
        puts("[3]-Mobiuz");
        puts("[4]-Ucell");
        puts("[5]-Humans");
        puts("[6]-Ortga qaytish");
        scanf("%d",&xizmat);
        switch(xizmat){
            case 1:
            printf("+99899"); 
             scanf("%d",&tel);
            if(tel<=9999999){
            printf("Tolov summasini kiriting :");
            scanf("%d",&tolov);
             puts("Tolov muvafaqqiyatli amalga oshirildi");   
             hisob-=tolov;
            }else{
                puts("Bunday raqam yoq !");
            }
            goto metka1;
            case 2:
            printf("+99893");
             scanf("%d",&tel);
            if(tel<=9999999){
            printf("Tolov summasini kiriting :");
            scanf("%d",&tolov);
             puts("Tolov muvafaqqiyatli amalga oshirildi");
             hisob-=tolov;   
            }else{
                puts("Bunday raqam yoq !");
            }
            goto metka1;
            case 3:
            printf("+99897"); 
            scanf("%d",&tel);
            if(tel<=9999999){
            printf("Tolov summasini kiriting :");
            scanf("%d",&tolov);
             puts("Tolov muvafaqqiyatli amalga oshirildi"); 
             hisob-=tolov;  
            }else{
                puts("Bunday raqam yoq !");
            }
            goto metka1;
            case 4:
            printf("+99894"); 
             scanf("%d",&tel);
            if(tel<=9999999){
            printf("Tolov summasini kiriting :");
            scanf("%d",&tolov);
             puts("Tolov muvafaqqiyatli amalga oshirildi");
             hisob-=tolov;   
            }else{
                puts("Bunday raqam yoq !");
            }
            goto metka1;
            case 5:
            printf("+99833");
            scanf("%d",&tel);
            if(tel<=9999999){
            printf("Tolov summasini kiriting :");
            scanf("%d",&tolov);
            hisob-=tolov;
             puts("Tolov muvafaqqiyatli amalga oshirildi");   
            }else{
                puts("Bunday raqam yoq !");
            }
            goto metka1;
            case 6:
            goto bosh;
            default :
            puts("Xizmat tanlashda xatolik");
            goto metka1;
        }
        case 3:
        metka2:
        puts("[1]-Uztelecom");
        puts("[2]-Turon telecom");
        puts("[3]-Sarkor telecom");
        puts("[4]-ortga qaytish");
        scanf("%d",&xizmat);
        switch(xizmat){
            case 1:
            puts("Iltimos litsevoy scetni kiriting :");scanf("%d",&scet);
            printf("Tolov miqdorini kiriting :");
            scanf("%d",&tolov);
            hisob-=tolov;
            puts("Tolov muvafaqqiyatli amalga oshirildi");
            goto metka2;
            case 2:
            puts("Iltimos litsevoy scetni kiriting :");scanf("%d",&scet);
            printf("Tolov miqdorini kiriting :");
            scanf("%d",&tolov);
            hisob-=tolov;
            puts("Tolov muvafaqqiyatli amalga oshirildi");
            goto metka2;
            case 3:
            puts("Iltimos litsevoy scetni kiriting :");scanf("%d",&scet);
            printf("Tolov miqdorini kiriting :");
            scanf("%d",&tolov);
            hisob-=tolov;
            puts("Tolov muvafaqqiyatli amalga oshirildi");
            goto metka2;
            case 4:
            goto bosh;
            default :
            puts("Xizmat tanlashda xatolik");
            goto metka2;
        }
        case 4:
        metka3:
         puts("Qancha pul yechmoqchisiz ");
         puts("[1] 50000  [2] 100000");
         puts("[3] 150000  [4] 200000");
         puts("[5] 300000  [6] 400000");
         puts("[7] Boshqa mablag");
         puts("[8]-Ortga qaytish");
         scanf("%d",&xizmat);
         switch(xizmat){
            case 1:
            hisob-=50000;
            puts("Operatsiya muvaffaqiyatli amalga oshirildi");
            puts("Mana pulingiz");
            goto metka3;
            case 2:
            hisob-=200000;
            puts("Operatsiya muvaffaqiyatli amalga oshirildi");
            puts("Mana pulingiz");
            goto metka3;
            case 3:
            hisob-=150000;
            puts("Operatsiya muvaffaqiyatli amalga oshirildi");
            puts("Mana pulingiz");
            goto metka3;
            case 4:
            hisob-=200000;
            puts("Operatsiya muvaffaqiyatli amalga oshirildi");
            puts("Mana pulingiz");
            goto metka3;
            case 5:
            hisob-=300000;
            puts("Operatsiya muvaffaqiyatli amalga oshirildi");
            puts("Mana pulingiz");
            goto metka3;
            case 6:
            hisob-=400000;
            puts("Operatsiya muvaffaqiyatli amalga oshirildi");
            puts("Mana pulingiz");
            goto metka3;
            case 7:
            printf("Summani kiriting :");scanf("%d",&summa);
            hisob-=summa;
            puts("Operatsiya muvaffaqiyatli amalga oshirildi");
            puts("Mana pulingiz");
            goto metka3;
            case 8:
            goto bosh;
            default :
            puts("Xizmat tanlashda xatolik");
            goto metka3;
         }
        case 5:
        metka4:
        printf("Balansingizda shuncha  %d mablag' bor\n",balans);
        puts("[1]-Yana biron bir amalni bajarmoqchi bolsangiz 1 ni bosing ");
        puts("[0]-Dasturdan chiqish uchun 0 ni bosing");
        scanf("%d",&xizmat);
        switch(xizmat){
            case 0:
            puts("Mana sizning kartangiz!");
            break;
            case 1:
            goto bosh;
            default :
            puts("Xizmat tanlashda xatolik");
            goto metka4;
        }
        case 6:
        printf("Tolov mobaynida shuncha %d mablag'ingiz qoldi!\n",hisob);
        puts("[1]-Yana biron bir amalni bajarmoqchi bolsangiz 1 ni bosing ");
        puts("[0]-Dasturdan chiqish uchun 0 ni bosing");
        scanf("%d",&xizmat);
        switch(xizmat){
            case 0:
            puts("Mana sizning kartangiz!");
            break;
            case 1:
            goto bosh;
            default :
            puts("Xizmat tanlashda xatolik");
            goto metka4;
        }
    }
}else if(parol!=pin){
    count++;
    if(count<3){
        goto qaytish;
    }
    puts("kartangiz bloklandi!!!");
    puts("7 kundan keyin bankdan ariza orqali olasiz!!!");
}
}
