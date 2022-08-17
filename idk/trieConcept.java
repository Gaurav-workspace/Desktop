class node{
    public node[] check;
    public boolean isEnd;
    public node(){
        this.check = new node[26];
        this.isEnd = false;
    }
}
class trie{
    private node root;
    public trie(){
        this.root = new node();
    }
    public void add(String s){
        int value;
        node temp = this.root;
        for (int i = 0; i < s.length(); i++) {
            value = s.charAt(i)-'a';
            if (temp.check[value]==null) {
                temp.check[value] = new node();
            }
            temp = temp.check[value];
        }
        temp.isEnd = true;
    }
    public boolean search(String s){
        int value;
        node temp = this.root;
        for (int i = 0; i < s.length(); i++) {
            value = s.charAt(i)-'a';
            if (temp.check[value]==null) {
                return false;
            }
            temp = temp.check[value];
        }
        return temp.isEnd;
    } 
}
public class trieConcept {
    public static void main(String[] args) {
        trie t = new trie();
        t.add("abc");
        t.add("abcd");
        t.add("gfg");
        System.out.println(t.search("gfg"));
        System.out.println(t.search("abcd"));
        System.out.println(t.search("abc"));
    }
}
