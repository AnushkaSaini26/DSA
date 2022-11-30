void sortColors(int* nums, int numsSize)
{
    int zero=0;
    int one=0;
    int two=0;
    int j ;
	

	for(j=0;j<numsSize;j++)
	{
		if (nums[j]==0)
		zero++;
		else if(nums[j]==1)
		one++;
		else
		two++;
	}
	int i=0;
	while(zero!=0)
	{
		nums[i]=0;
		i++;
		zero--;
		
	}
	while(one!=0)
	{
		nums[i]=1;
		i++;
		one--;
	}
	while(two!=0)
	{
		nums[i]=2;
		i++;
		two--;
	}
	for(j=0;j<numsSize;j++)
	printf("%d ",nums[j]);


}
