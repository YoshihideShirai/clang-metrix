int add(int a, int b) {
    return a + b;
}

int max(int a, int b) {
    if (a > b)
        return a;
    else
        return b;
}

void loop(int n) {
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0)
            continue;
    }
}

int sample(int a, int b) {
    int sum = 0;
    if (a > b) {
        sum = a - b;
    } else {
        sum = b - a;
    }
    return sum;
}

void calculate_average()
{
    int a, b, c, avg;
    scanf("%d %d %d", &a, &b, &c);
    avg = (a + b + c) / 3;
    printf("avg = %d", avg);
}

void switch_cases1(int a){
    switch (a) {
        case 1:
            printf("Case 1\n");
            break;
        case 2:
            printf("Case 2\n");
            break;
        case 3:
            printf("Case 3\n");
            break;
        default:
            printf("Default case\n");
    }
}

void switch_cases(int a){
    switch (a) {
        case 1:
            printf("Case 1\n");
            break;
        case 2:
            printf("Case 2\n");
            break;
        default:
            printf("Default case\n");
    }
}
