class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Initialize the total time required to 0
        total_time = 0
      
        # Iterate over the ticket queue to simulate the time passing
        for index, val in enumerate(tickets):
            # If the current position is before or at the target position k
            if index <= k:
                # Add the minimum of the target tickets and tickets at the current position
                # It ensures we do not count the extra tickets the target person doesn't need
                total_time += min(tickets[k], val)
            else:
                # After the target person has bought their tickets, they will not buy more 
                # Thus, for the people after the target, we consider one less ticket for the target
                # Person at position k would have already bought their ticket when turn comes to later positions
                total_time += min(tickets[k] - 1, val)
      
        # Return the calculated total time
        return total_time      