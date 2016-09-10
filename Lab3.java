public class Lab3
{
 public static void main(String [] args)
 {
  System.out.println("m     "  + "  n  " + "  p  " + " q " +" r "+ " Is it Satisfied?");
  for (int mm= 0; mm<= 1; mm++)
     for(int nn = 0; nn <=1; nn++)
       for(int pp = 0; pp <=1; pp++)
        for(int qq = 0; qq <=1; qq++)
         for(int rr = 0; rr <=1; rr++)
       {
         boolean m,n,p,q,r, satisfy;
         m = ( mm == 1 );
         n = (nn == 1);
         p = (pp ==1 );
         q = (qq ==1 );
         r = (rr == 1);
         satisfy = ( (p || !q) && (m || !n || q || r) && (!m || !n || p || r) && (!n || !q || !r) == true );
         if ((p || !q) && (m || !n || q || r) && (!m || !n || p || r) && (!n || !q || !r)){ 
          System.out.println(m + "  " + n + "  " + p + "  " + q + "   " + r +"    " + satisfy );
         }
         }
 }
}