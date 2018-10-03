#ifndef aho_corasick_hpp
#define aho_corasick_hpp
 
#include <queue>
#include <string>
#include <vector>
#include <set>
 
namespace MB
{
 
namespace detail
{
 
// Maximum number of characters in alphabet
static constexpr int MAXCHARS = 256;
 
struct state
{
    std::set<int> output_function;
    int failure_function;
    std::vector<int> goto_function;
    state()
        : failure_function(-1),
          goto_function(detail::MAXCHARS, -1)
    {
    }
};
 
} // namespace detail
 
class ac_automaton
{
public:
    template <class InputIt>
    ac_automaton(InputIt first, InputIt last)
        : states(1)
    {
        // Build the prefix tree
        for (InputIt it = first; it != last; ++it) {
            add_word(*it);
        }
        // Turn it into an automaton
        construct_automaton();
    }
 
    template <class OutputIt>
    OutputIt search(std::string text, OutputIt it) const
    {
        int current_state = 0;
      
        for (int i = 0; i < text.size(); ++i) {
            current_state = find_next_state(current_state, text[i]);
            if (states[current_state].output_function.size()) {
                for (auto length : states[current_state].output_function) {
                    *it++ = std::make_pair(std::string(text, i - length + 1, length),
                            i - length + 1);
                }
            }
        }
        return it;
    }
 
private:
    std::vector<detail::state> states;
 
private:
    void add_word(const std::string &word)
    {
        int current_state = 0;
        // Add to prefix tree
        for (int c : word) {
            if (states[current_state].goto_function == -1) {
                states[current_state].goto_function = states.size();
                states.push_back(detail::state());
            }
            current_state = states[current_state].goto_function;
        }
        // Add to output function for this state
        states[current_state].output_function.insert(word.size());
    }
 
    void construct_automaton()
    {
        // Complete the goto function by setting it to 0 for each
        // letter that doesn't have an edge from the root
        for (int c = 0; c < detail::MAXCHARS; ++c) {
            if (states[0].goto_function == -1) {
                states[0].goto_function = 0;
            }
        }
      
        // Compute failure and output functions
        std::queue<int> state_queue;
        for (int c = 0; c < detail::MAXCHARS; ++c) {
            if (states[0].goto_function != 0) {
                states[states[0].goto_function].failure_function = 0;
                state_queue.push(states[0].goto_function);
            }
        }
        while (state_queue.size()) {
            int s = state_queue.front();
            state_queue.pop();
      
            for (int c = 0; c < detail::MAXCHARS; ++c) {
                if (states[s].goto_function != -1) {
                    int failure = states[s].failure_function;
                    while (states[failure].goto_function == -1) {
                         failure = states[failure].failure_function;
                    }
                    failure = states[failure].goto_function;
                    states[states[s].goto_function].failure_function = failure;
                    for (auto length : states[failure].output_function) {
                        states[states[s].goto_function].output_function.insert(length);
                    }
                    state_queue.push(states[s].goto_function);
                }
            }
        }
    }
  
    int find_next_state(int current_state, char c) const
    {
        int next_state = current_state;
      
        while (states[next_state].goto_function == -1) {
            next_state = states[next_state].failure_function;
        }
      
        return states[next_state].goto_function;
    }
  
};
 
} // namespace MB
 
#endif // AHO_CORASICK_HPP