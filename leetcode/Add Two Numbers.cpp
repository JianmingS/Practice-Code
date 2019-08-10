/*
 
 * */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* tmp = head;
    int carry = 0;
    while(true) {
        int val = carry;
        if (l1) {
            val += l1->val;
            l1 = l1->next;
        }
        if(l2) {
            val += l2->val;
            l2 = l2->next;
        }       
        tmp->val = val%10;
        carry = val/10;
        
        if (l1 || l2 || carry) {
            tmp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            tmp = tmp->next;
        }else {
            tmp->next = NULL; // Ïê¼û×¢ÊÍ
            break;
        }
    }
    return head;
}
