class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # rows[y] will store a difference array along x-axis for this y-coordinate
        rows = defaultdict(lambda: defaultdict(int))
        
        for x1, y1, x2, y2 in rectangles:
            start_row = rows[y1]
            end_row = rows[y2]
            
            start_row[x1] += 1
            start_row[x2] -= 1
            end_row[x1] -= 1
            end_row[x2] += 1
        
        active_x = defaultdict(int)  # tracks cumulative coverage of x-positions at current row
        widths = set()               # stores horizontal widths at each row 
        sorted_y_coords = sorted(rows)  # process rows from bottom to top

        for y in sorted_y_coords:
            running_count = 0
            # Debug: uncomment to see active x coverage per row
            # print(y, ":", end=" ")
            
            # Iterate through current active x-positions in order
            positions = sorted(active_x)
            for pos in positions:
                if running_count == 0:
                    start_x = pos
                running_count += active_x[pos]
                
                # Overlap detected horizontally
                if running_count > 1:
                    return False
                
                # End of a continuous interval
                if running_count == 0:
                    end_x = pos
                    # Debug: print the horizontal interval at this row
                    # print(start_x, end_x, end=" ")
                    
                    # Ensure all horizontal spans are identical
                    widths.add((start_x, end_x))
                    if len(widths) > 1:
                        return False
            # print()  

            # Update active_x with difference array for this row
            row = rows[y]
            for pos  in row:
                active_x[pos] += row[pos]
                if active_x[pos] == 0:
                    active_x.pop(pos)
                    
        return True
