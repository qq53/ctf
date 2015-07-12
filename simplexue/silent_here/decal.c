/// \file 1.c
/*
  ------------------------------------
  Create date : 2015-07-12 05:35
  Modified date: 2015-07-13 04:21
  Author : Sen1993
  Email : gsen1993@gmail.com
  ------------------------------------
*/

int main(){
	int i;
	unsigned int j, k, eax, ebx2, ebx3, ecx, cl, edx, esi1, esi2, edi, ebp2;
	k = 0x0BF7A7C9 - 0x9E147749;
	j = 0x1CDDB7B9 - 0xD4181073;
	ebp2 = 0x0E3D8E84;
	ebx3 = 0x5B001E42;
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
	i = sizeof(arr)/sizeof(arr[0])-1;
	while(i > 0){
		eax = (j*2+1)*j;
		edx = (eax>>27) + (eax<<5);
		eax = (k*2+1)*k;
		esi1 = (eax>>27) + (eax<<5);
		eax = ebp2 - arr[i-1];
		cl = esi1 & 0x1f;
		edi = (eax << (32-cl)) + (eax >> cl);
		ecx = edx ^ edi;
		ebx2 = ebx3 - arr[i];
		esi2 = (ebx2>>edx)+(ebx2<<(32-edx));

		ebp2 = k;
		k = esi1 ^ esi2;
		ebx3 = j;
		j = ecx;
		i -= 2;
	}
	printf("%08X%08X%08X%08X\n", ecx, ebx3-0x63D4757A, k, ebp2-0xEE7A3CB4);
}
