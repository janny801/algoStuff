#include <iostream>
#include <vector>
#include <cstdlib>  // rand
#include <ctime>    // time
using namespace std;

/*
    quickSelect:
    - Takes the array BY VALUE (local copy), so the caller's array is not modified.
    - Iterative quick-select to find the element with rank kIndex (0-indexed).
    - Expected O(n) time due to randomized pivot selection.
*/
int quickSelect(vector<int> localCopy, int kIndex)
{
    int leftIndex = 0;
    int rightIndex = static_cast<int>(localCopy.size()) - 1;

    while (true)
    {
        // If the search range has collapsed to a single element, return it.
        if (leftIndex == rightIndex)
        {
            return localCopy[leftIndex];
        }

        // Choose a random pivot to avoid worst-case behavior on structured inputs.
        int pivotIndex = leftIndex + rand() % (rightIndex - leftIndex + 1);
        int pivotValue = localCopy[pivotIndex];

        // Partition (Lomuto style) around pivotValue.
        // Move pivot to end, then bring all smaller elements to the front.
        swap(localCopy[pivotIndex], localCopy[rightIndex]);
        int storeIndex = leftIndex;
        for (int i = leftIndex; i < rightIndex; i++)
        {
            if (localCopy[i] < pivotValue)
            {
                swap(localCopy[storeIndex], localCopy[i]);
                storeIndex++;
            }
        }
        // Place pivot in its final position.
        swap(localCopy[storeIndex], localCopy[rightIndex]);

        // Narrow the search range based on the pivot's final position.
        if (kIndex == storeIndex)
        {
            return localCopy[storeIndex];
        }
        else if (kIndex < storeIndex)
        {
            rightIndex = storeIndex - 1;
        }
        else
        {
            leftIndex = storeIndex + 1;
        }
    }
}

/*
    quarterDuplicateValues:
    - Returns true if some value appears strictly more than n/4 times.
    - Logic:
        1) If an element occurs > n/4 times in sorted order, it must appear at
           ranks floor(n/4), floor(n/2), or floor(3n/4).
        2) Use quick-select (on BY-VALUE copies) to get those three candidates.
        3) Do one linear pass to count those candidates in the original array.
        4) If any count > n/4, return true.
    - No pass-by-reference is used anywhere (Rhythm-friendly).
*/
bool quarterDuplicateValues(vector<int> inputArray)
{
    int arraySize = static_cast<int>(inputArray.size());
    if (arraySize == 0)
    {
        return false;
    }

    // Seed RNG once for randomized pivot selection in quick-select.
    srand(static_cast<unsigned>(time(nullptr)));

    // Compute the three relevant ranks (0-indexed).
    int rankQuarter = arraySize / 4;          // floor(n/4)
    int rankHalf = arraySize / 2;             // floor(n/2)
    int rankThreeQuarter = (3 * arraySize) / 4; // floor(3n/4)

    // Get candidates at those positions (each call copies internally).
    int candidateQuarter = quickSelect(inputArray, rankQuarter);
    int candidateHalf = quickSelect(inputArray, rankHalf);
    int candidateThreeQuarter = quickSelect(inputArray, rankThreeQuarter);

    // Build a small unique list of candidates to verify.
    vector<int> uniqueCandidates;
    uniqueCandidates.push_back(candidateQuarter);
    if (candidateHalf != candidateQuarter)
    {
        uniqueCandidates.push_back(candidateHalf);
    }
    if (candidateThreeQuarter != candidateQuarter && candidateThreeQuarter != candidateHalf)
    {
        uniqueCandidates.push_back(candidateThreeQuarter);
    }

    // Verify actual counts in one pass over the original input.
    vector<int> candidateCounts(uniqueCandidates.size(), 0);
    for (int currentValue : inputArray)
    {
        for (size_t i = 0; i < uniqueCandidates.size(); i++)
        {
            if (currentValue == uniqueCandidates[i])
            {
                candidateCounts[i]++;
            }
        }
    }

    // Check strictly more than floor(n/4).
    int thresholdExclusive = arraySize / 4;
    for (int countValue : candidateCounts)
    {
        if (countValue > thresholdExclusive)
        {
            return true;
        }
    }
    return false;
}

/*
    Tiny demo. Replace with your own test harness or remove main() for submission.
*/
int main()
{
    vector<int> sampleInput = {1, 2, 3, 1, 1, 4, 1, 5, 1, 2, 2, 2, 2};
    vector<int> allSame = {7,7,7,7,7};
    vector<int> noHeavy = {1,2,3,4,5,6,7,8};

    cout << boolalpha;

    cout << quarterDuplicateValues(sampleInput) << "\n"; // expected: true
    cout << quarterDuplicateValues(allSame) << "\n";     // expected: true
    cout << quarterDuplicateValues(noHeavy) << "\n";     // expected: false
}
