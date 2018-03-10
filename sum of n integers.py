#include<stdio.h>
int main()
{
int a[0],i,n,k,sum=0;
printf("enter the limit of natural numbers");
printf("  \nenter upto what u have to sum ");
scanf("%d%d",&n,&k);
for(i=1;i<=n;i++)
{
 scanf("%d",&a[i]);   
}
for(i=0;i<=k;i++)
{
sum=sum+i;
}
printf("%d",sum);
}
