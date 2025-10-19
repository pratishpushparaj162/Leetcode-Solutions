/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    if(!head || !head.next) return head;
    let sentinel = new ListNode(); //add dummy node in front of list
    let prev = sentinel; 
    let cur = head;
    let next = head.next;
      
    //dummy(prev)->1(cur)->2(next)->3->4
    //1. connect prev to next
    //2. now connect cur(first value) to next->next
    //3. connect next(second value) to prev

  
    //dummy->2->1->3->4  :first iteration
    //dummy->2->1->4->3. :second iteration
    
    while(cur && next) {
        prev.next = next; 
        cur.next = next.next;
        next.next = cur;
        prev = cur;
        cur = prev.next;
        if(cur) {
            next = cur.next;
        }
    }

    return sentinel.next;
    
};
