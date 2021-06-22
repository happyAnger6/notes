#include <stack>

using namespace std;

int get_num(string s, int *pi)
{
    int i = *pi;
    int num = 0;
    char sign = '+';
    while(i < s.size())
    {
        c = s[i];
        if(c == '+')
            sign = '+';
        else if(c == '-')
            sign = '-';
        else if('0' <= c && c <= '9')
            num = num * 10 + c - '0';
        else
            break;
        i+=1;
    }

    *pi = i;
    if (sign == '-')
        return -num;
    return num;
}

int caculate(string s, int *pi)
{
    stack<int> results;
    char sign = '+';

    int num = 0;
    int i = *pi;
    int size = s.size();
    int sum = get_num(s, &i);
    while (i < size) {
        c = s[i];
        if (c == '+' || c == '-' || c == '/' || c == '*') 
        {
            sign = c;
            i+=1;

            if (c == '/') {
                int top = stack.top();
                stack.pop();
                stack.push(top / num);
            }
            else if (c == '*') {
                int top = stack.top();
                stack.pop();
                stack.push(top * num);
            }
            else {
                if (sign == '-')
                    stack.push(-num);
                else
                    stack.push(num);
            }
        }
        if (c == '(') {
            num = caculate(s, &i);
            stack.push(num);
        }
        else if (c == ')') {
            i+=1;
            *pi = i;
            break;
        }
    }

    while(!stack.empty()) {
        int top = stack.top();
        stack.pop();
        sum += top;
    }

    return sum;
}