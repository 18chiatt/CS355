function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    const stack = []
    let index1 = 0;
    let index2 = 0;
    while((index1 < m) || (index2 < n)){
        const index1Valid = index1 < m;
        const index2Valid = index2 < n;
        let lowest = -Infinity;
        let toIncrement = 0;
        if(index1Valid && nums1[index1] < lowest) {
            lowest = nums1[index1]
            toIncrement = 1;
        }
        if(index2Valid && nums2[index2] < lowest){
            lowest = nums2[index2]
            toIncrement = 2
        }
        stack.push(lowest);
        toIncrement === 1 ? index1++ : index2++
    }

    for(let i =0; i< stack.length; i++){
        nums1[i] = stack[i]
    }
                                                                             
};

const a =[1,2,3,0,0,0]
const m = 3
const n2 = [2,5,6]
const n = 3

merge(a,m,n2,n)