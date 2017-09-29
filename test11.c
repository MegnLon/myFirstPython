char c[] //存放数组的
int len=strlen(c)  //获取数组长度
int i,j;
char temp; //存放临时变量
for( i=0;i<len;i++)
{
	for( j=0;j<len-i-1;j++)
	{
		if(c[j]>c[j+1])  //判断第一个是否大于第二个，是就交换，所以这个是按从低到高排序
		{
			temp=c[j+1];
			c[j+1]=c[j];
			c[j]=temp;
		}
	}
}