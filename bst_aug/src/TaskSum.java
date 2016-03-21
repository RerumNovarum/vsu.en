import java.io.*;
import java.util.Scanner;

public class TaskSum {
    public static final String TASK = "sum";
    private static final boolean FILE_IO = true;

    public static void main(String[] args) throws IOException {
        InputStream in;
        OutputStream out;

        if (FILE_IO) {
            in = new FileInputStream(TASK + ".in");
            out = new FileOutputStream(TASK + ".out");
        } else {
            in = System.in;
            out = System.out;
        }

        Scanner scanner = new Scanner(new BufferedInputStream(in));
        PrintWriter writer = new PrintWriter(out);
        // --
        int N = scanner.nextInt();
        int K = scanner.nextInt();

        SegmentTree st = new SegmentTree();

        for (int k = 0; k < K; k++) {
            String cmd = scanner.next();
            int i = scanner.nextInt();
            int j = scanner.nextInt();
            if (cmd.equals("A"))
                st.put(i, j);
            else if (cmd.equals("Q"))
                writer.println(st.sum(i, j));

        }
        // --
        writer.flush();
    }

    public static class SegmentTree {
        public static final boolean RED = true, BLACK = false;

        private Node root;

        public void put(int key, int val) {
            root = put(root, key, val);
            root.color = BLACK;
        }
        private Node put(Node r, int key, long val) {
            if (r == null) return new Node(key, val);

            int cmp = Long.compare(key, r.key);
            if (cmp == 0) r.val = val;
            else if (cmp < 0) r.left = put(r.left, key, val);
            else r.right = put(r.right, key, val);

            repair(r);

            if(!isRed(r.left) && isRed(r.right))
                r = rotateLeft(r);
            if(isRed(r.left) && isRed(r.left.left))
                r = rotateRight(r);
            if(isRed(r.left) && isRed(r.right))
                flipColors(r);

            return r;
        }

        public long sum(int from, int to) {
            return sum(root, from, to);
        }
        private long sum(Node r, int from, int to) {
            if (r == null) return 0;

            if (contains(from, to, r.from, r.to))
                return r.sum;
            if (intersects(from, to, r.from, r.to)) {
                long sum;
                sum = intersects(r.key, r.key, from, to) ? r.val : 0;
                sum += sum(r.left, from, to);
                sum += sum(r.right, from, to);
                return sum;
            }
            return 0;
        }

        private boolean intersects(int from1, int to1, int from2, int to2) {
            return (from1 <= from2 && from2 <= to1) ||
                    (from2 <= from1 && from1 <= to2);
        }
        private boolean contains(int from1, int to1, int from2, int to2) {
            return from1 <= from2 && from2 <= to2 && to2 <= to1;
        }



        private void flipColors(Node n) {
            n.left.color = n.right.color = n.color;
            n.color = RED;
        }
        private Node rotateLeft(Node n) {
            Node x = n.right;
            n.right = x.left;
            x.left = n;

            fixRotation(n, x);
            return x;
        }
        private Node rotateRight(Node n) {
            Node x = n.left;
            n.left = x.right;
            x.right = n;

            fixRotation(n, x);
            return x;
        }
        private void fixRotation(Node n, Node x) {
            x.color = n.color;
            n.color = RED;
            repair(n);
            repair(x);
        }
        private void repair(Node n) {
            int from, to;
            long sum;
            from = to = n.key;
            sum = n.val;

            if (n.left != null) {
                from = n.left.from;
                sum += n.left.sum;
            }
            if (n.right != null) {
                to = n.right.to;
                sum += n.right.sum;
            }

            n.from = from;
            n.to = to;
            n.sum = sum;
        }
        private boolean isRed(Node n) {
            return n != null && n.color == RED;
        }

        private static class Node {
            public int from, to, key;
            public long sum;
            public long val;
            public boolean color = RED;
            public Node left, right;

            public Node(int key, long val) {
                this.val = this.sum = val;
                this.from = this.to = this.key = key;
            }
        }
    }
}
