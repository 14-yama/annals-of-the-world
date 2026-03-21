import React, { useState } from 'react'
import { Box, SimpleGrid, Text, Flex, Heading } from '@chakra-ui/react'
import { Brain, Trophy, ChevronRight, BookOpen, RotateCcw } from 'lucide-react'
import { QUIZ_SESSIONS } from '../data/quizzes'
import QuizEngine from '../components/QuizEngine'
import { SectionHeading } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'
import type { QuizSession } from '../types'

const DIFFICULTY_COLORS: Record<string, string> = {
  beginner: '#38A169',
  intermediate: '#D4AF37',
  advanced: '#D44',
  expert: '#6B3FA0',
}

export default function QuizPage() {
  const [activeSession, setActiveSession] = useState<QuizSession | null>(null)

  if (activeSession) {
    return (
      <Box>
        {/* Back to quiz selection */}
        <Flex
          align="center" gap={2} mb={6} cursor="pointer"
          color="#9E9A90" onClick={() => setActiveSession(null)}
          _hover={{ color: '#D4AF37' }}
        >
          <RotateCcw size={16} />
          <Text fontSize="sm">Back to Quiz Selection</Text>
        </Flex>

        <QuizEngine session={activeSession} onComplete={() => setActiveSession(null)} />
      </Box>
    )
  }

  return (
    <Box>
      <Breadcrumb items={[{ label: 'Examination Hall' }]} />
      {/* Page Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Brain size={28} color="#6B3FA0" />
          <Heading fontFamily='"Cinzel", serif' fontSize="3xl" fontWeight={700} color="#2D2A24">
            History Quiz
          </Heading>
        </Flex>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" color="#524E44" maxW="600px">
          Test your knowledge of world history — from prehistory to the digital age.
          Choose a quiz below to begin your journey through time.
        </Text>
        <Box h="3px" bg="#6B3FA0" w="80px" mt={4} />
      </Box>

      {/* Quiz Stats */}
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={8}>
        <Box bg="#F5F4F0" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4} position="relative" overflow="hidden">
          <Box position="absolute" top={0} left={0} w="4px" h="100%" bg="#38A169" />
          <Text fontSize="2xl" fontWeight={700} color="#38A169" fontFamily='"Cinzel", serif'>
            {QUIZ_SESSIONS.find(s => s.difficulty === 'beginner')?.questions.length ?? 0}
          </Text>
          <Text fontSize="sm" color="#524E44">Beginner Questions</Text>
        </Box>
        <Box bg="#F5F4F0" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4} position="relative" overflow="hidden">
          <Box position="absolute" top={0} left={0} w="4px" h="100%" bg="#D4AF37" />
          <Text fontSize="2xl" fontWeight={700} color="#D4AF37" fontFamily='"Cinzel", serif'>
            {QUIZ_SESSIONS.find(s => s.difficulty === 'intermediate')?.questions.length ?? 0}
          </Text>
          <Text fontSize="sm" color="#524E44">Intermediate Questions</Text>
        </Box>
        <Box bg="#F5F4F0" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4} position="relative" overflow="hidden">
          <Box position="absolute" top={0} left={0} w="4px" h="100%" bg="#D44" />
          <Text fontSize="2xl" fontWeight={700} color="#D44" fontFamily='"Cinzel", serif'>
            {QUIZ_SESSIONS.find(s => s.difficulty === 'advanced')?.questions.length ?? 0}
          </Text>
          <Text fontSize="sm" color="#524E44">Advanced Questions</Text>
        </Box>
        <Box bg="#F5F4F0" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4} position="relative" overflow="hidden">
          <Box position="absolute" top={0} left={0} w="4px" h="100%" bg="#6B3FA0" />
          <Text fontSize="2xl" fontWeight={700} color="#6B3FA0" fontFamily='"Cinzel", serif'>
            {QUIZ_SESSIONS.find(s => s.difficulty === 'expert')?.questions.length ?? 0}
          </Text>
          <Text fontSize="sm" color="#524E44">Expert Questions</Text>
        </Box>
      </SimpleGrid>

      {/* Quiz Sessions */}
      <SectionHeading title="Choose Your Challenge" subtitle="6 curated quiz sessions across all eras and difficulty levels" />
      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={5} mb={8}>
        {QUIZ_SESSIONS.map(session => {
          const color = DIFFICULTY_COLORS[session.difficulty] ?? '#8B3A3A'
          return (
            <Box
              key={session.id}
              bg="white" border="1px solid" borderColor="#E4E2DC"
              borderRadius="xl" overflow="hidden" cursor="pointer"
              transition="all 0.3s"
              _hover={{ borderColor: color, transform: 'translateY(-3px)', boxShadow: '0 8px 24px rgba(0,0,0,0.1)' }}
              onClick={() => setActiveSession(session)}
            >
              {/* Color bar */}
              <Box h="4px" bg={color} />

              <Box p={5}>
                <Flex justify="space-between" align="flex-start" mb={3}>
                  <Box>
                    <Text fontFamily='"Cinzel", serif' fontSize="lg" fontWeight={700} color="#2D2A24">
                      {session.title}
                    </Text>
                    <Flex align="center" gap={2} mt={1}>
                      <Text
                        fontSize="xs" fontWeight={700} color={color}
                        bg={`${color}15`} px={2} py={0.5} borderRadius="full"
                        textTransform="capitalize"
                      >
                        {session.difficulty}
                      </Text>
                      <Text fontSize="xs" color="#9E9A90">
                        {session.questions.length} questions
                      </Text>
                    </Flex>
                  </Box>
                  <Trophy size={20} color={color} />
                </Flex>

                <Text fontSize="sm" color="#524E44" lineHeight={1.5} mb={4}>
                  {session.description}
                </Text>

                {session.era && (
                  <Flex align="center" gap={1.5} mb={2}>
                    <BookOpen size={12} color="#96770B" />
                    <Text fontSize="xs" color="#96770B">Era: {session.era}</Text>
                  </Flex>
                )}

                <Flex
                  align="center" justify="center" gap={2}
                  bg={color} color="white" borderRadius="lg"
                  py={2.5} fontWeight={600} fontSize="sm"
                  transition="opacity 0.2s" _hover={{ opacity: 0.9 }}
                >
                  Start Quiz <ChevronRight size={16} />
                </Flex>
              </Box>
            </Box>
          )
        })}
      </SimpleGrid>

      {/* How It Works */}
      <Box bg="#F5F4F0" borderRadius="lg" p={6} border="1px solid" borderColor="#E4E2DC">
        <Text fontSize="sm" color="#524E44" fontWeight={600}>How It Works</Text>
        <Text fontSize="sm" color="#524E44" mt={2} lineHeight={1.6}>
          Each quiz presents multiple-choice questions drawn from the Annals knowledge graph.
          After selecting an answer, you'll see whether you were correct along with a detailed explanation.
          Your score is tallied at the end with a breakdown by question. Questions cover all 8 eras,
          14 regions, and range from beginner (general knowledge) to expert (Annals schema deep dives).
        </Text>
      </Box>
    </Box>
  )
}
