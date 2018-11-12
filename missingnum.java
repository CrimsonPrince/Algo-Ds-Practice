public class missingnum {


	public static void main(String []args)
	{
		int[] mylist = {1,2,3,4,5,6,7,8,10};

		for(int i=0;i < mylist.length;i++)
		{
			if(mylist[i] - mylist[i + 1] > 1)
			{
				System.out.println(mylist[i] - 1);
			}
		}

	}

}
