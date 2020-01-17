
//#define SIZE 50
//
//
//Command queue[SIZE];
//int beginIndex = 0;
//int endIndex = 0;
//int elements = 0;
//
///*
// * Gets next input from the queue
// */
//Command getNextInput() {
//  Command got = queue[beginIndex];
//  beginIndex = (beginIndex + 1) % SIZE;
//  elements--;
//  return got;
//}
//
///*
// * Adds input to end of queue
// */
//Command addToQueue(Command toAdd) {
//  queue[endIndex] = toAdd;
//  endIndex = (endIndex + 1) % SIZE;
//  elements++;
//}
//
///*
// * Returns number of elements in queue 
// */
//int getQueueLength() {
//  return elements;
//}
//
///*
// * Returns true if queue has next element
// */
//bool queueHasNextElement() {
//  return elements > 0;
//}
