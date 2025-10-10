class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode small = new ListNode(-1);
        ListNode large = new ListNode(-1);
        ListNode temp1 = small;
        ListNode temp2 = large;
        while(head!=null){
            if(head.val<x){
                temp1.next=head;
                temp1=head;
            }else{
                temp2.next=head;
                temp2=head;
            }
            head=head.next;
        }
        temp2.next=null;
        temp1.next=large.next;
        return small.next;
    }
}
