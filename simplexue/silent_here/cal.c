/// \file 3.c
/*
  ------------------------------------
  Create date : 2015-07-12 17:40
  Modified date: 2015-07-13 04:00
  Author : Sen1993
  Email : gsen1993@gmail.com
  ------------------------------------
*/
int main(){
	unsigned int ecx, ebx, edx, ebp, eax, edi, esi;
	int j,k;
	ecx = ebx = edx = ebp = 0;
	k = edx;
	edx = 0x63D4757A;
	ebx += 0x63D4757A;
	ebp += 0xEE7A3CB4;
	unsigned int arr[] = {0x6D00027A,
		0x8831B70F,    0x7728D975,    0xE7BA4156,    0xDC92BFAD,
		0xCB17967B,    0x1F8B0D7A,    0x8E0B0D4F,    0x431C9651,
		0x22293C7F,    0x0D243845,    0xC23C7BA6,    0x4CAD232E,
		0xB35D36FF,    0x551BC015,    0x0BF3CF67,    0xDDAF2D46,
		0xA72AA80D,    0xEC1C33D4,    0x896B736B,    0x189D7F20,
		0xE46D20BE,    0xC4DDD5CC,    0x3DBBA1A7,    0x8A692DB8,
		0xEEB598C4,    0x0AA88B0C,    0xF506A11A,    0xADC68F57,
		0x1739E928,    0x577803DA,    0x958F416A,    0xDF1C7CA7,
		0x0BBAD3FE,    0xAB6DB39C,    0xB8048075,    0x92628ABB,
		0x5CEB9507,    0x64CCA67C,    0xD00B10A6};
	int len = sizeof(arr)/sizeof(arr[0]);
	int i = 1;
	while(i < len){
		if( i != 1 )
			ecx = j;
		eax = (ebx*2+1)*ebx;
		edx = (eax >> 27) + (eax << 5);
		eax = (ebp*2+1)*ebp;
		esi = (eax >> 27) + (eax << 5);
		edi = edx ^ ecx;
		ecx = 32;
		eax = esi & 0x1f;
		edx = edx & 0x1f;
		j = ebx;
		eax = (edi >> (32-eax)) + (edi << eax);
		eax = eax + arr[i-1];
		esi = esi ^ k;
		k = ebp;
		ebp = eax;
		ebx = (esi << edx) + (esi >> (32-edx));
		ebx = ebx + arr[i];
		i += 2;
	}
	edx = k + 0x9E147749;
	esi = j + 0xD4181073;
	printf("%08X %08X %08X %08X\n",esi, ebx, edx, eax);
}
