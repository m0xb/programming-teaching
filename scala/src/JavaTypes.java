public class JavaTypes {

    class Person {
        String name;
        Person(String name) {}
    }

    static class IntBox {
        int value;
        IntBox(int value) {
            this.value = value;
        }
    }

    public static void main(String[] args) {
        // In memory: 00000000000000000000000101
        int x = 5;
        //x * 2;

        // In memory: 00000000000000000000000101
        int z = 5;

        // A reference to memory on the heap
        // In memory: 101010101010101010001011100 --> pointing to a mem address
        IntBox y = new IntBox(5);
        System.out.println(y.value * 2);



//        Object foo = Person("Sim");
//        foo.name

    }
}

/*

0000
0001
0010
0011
0100
0101
0110
0111
1000
1001 = 9

8 + 4 + 2
1110 = 14

27  11  3  3  1
16 + 8  _  2  1
1    1   0 1  1

111   47   15 15   7  3
 64 + 32 + _ + 8 + 4 + 2 + 1
 1101111


0000 1011 0001 0010
      ADD    1    2
      1+2
      (+ 1 2) <-- lisp :-)





 */