class Solution {
    public void remove(ListNode prev,ListNode curr, int val)
    {
         if(curr.next!=null)
            remove(curr,curr.next,val);  
         if(curr.val==val)
            prev.next=curr.next;
    }
    public ListNode removeElements(ListNode head, int val) {
       if(head==null) return null;
       
       ListNode dummy=new ListNode(-1);
       dummy.next=head;
       remove(dummy,head,val);
       return dummy.next;
    }
}
