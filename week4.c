#include <stdio.h>
int level;
int expt;
int quant;
int calc()
{
	printf("레벨을 입력하세요 : ");
	scanf("%d", &level);
	printf("경험치를 입력하세요 : ");
	scanf("%d", &expt);
	printf("재료의 기본 양을 입력하세요 : ");
	scanf("%d", &quant);
	return quant*(level + expt);
}
void making(total)
{
	printf("재료의 필요 양: %d\n", total);
	printf("포션 제조 완료!");
}
int main()
{
	int vari = calc();
	making(vari);
}
